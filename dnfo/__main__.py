#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""display info from the Dnd 5th edition API"""
from __future__ import annotations
import sys
from typing import Any, TypedDict
import requests
from rich import print
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from dnfo import BASE_URL, ENDPOINTS, SECONDARIES, __version__
from dnfo.database_ops.clear import clear_db
from dnfo.database_ops.populate import populate_db


# pylint: disable=R0903
# TODO update this with some optionals for the different index types
class EndpointResponse(TypedDict):
    """dictionary typing for the response of any endpoint"""

    count: int
    results: list[dict[str, str]]


def get_args():
    """get arguments with sys.argv
    argument format is: endpoint, index
    """
    if len(sys.argv) == 1 or (set(["-h", "--help", "help"]) & set(sys.argv)):
        usage()
    elif set(["-v", "--version"]) & set(sys.argv):
        print(f"[white]dnfo v{__version__}")
        sys.exit()
    elif len(sys.argv) > 3 and sys.argv[1] not in SECONDARIES:
        print(f"{sys.argv[1]} only supports one index as an argument.")
        usage(1)
    args: list[str] = sys.argv[1:]
    return args


def check_endpoint(endpoint: str):
    """check if the endpoint given is valid"""
    if endpoint.casefold() not in ENDPOINTS:
        print("Invalid endpoint! Options are:")
        print(Columns(ENDPOINTS, expand=True))
        sys.exit(1)


def query_api(endpoint: str, index=None):
    """query an endpoint for its available indexes"""
    url: str = f"{BASE_URL}/{endpoint}"
    if index:
        url += f"/{index}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error. Either {index} is not a valid index or {endpoint} is invalid.")
        usage(1)
    response = response.json()
    return response


def print_index_options(response: EndpointResponse, endpoint: str):
    """print available indexes for a given endpoint"""
    index_options: list[str] = []
    for name in range(response["count"]):
        index_options.append(response["results"][name]["index"])
    del response
    print(f"Possible indexes for {endpoint}:")
    print(Panel(Columns(index_options, expand=True), title=f"Indexes for {endpoint}"))
    print(
        f"Run 'dnfo {endpoint} \\[index]' to get info on a {make_singular(endpoint)}!"
    )


def print_index(index: dict[str, Any]):
    """format the information of a dictionary to a rich Table and print"""
    # for debugging: print(index)
    table = Table(title=index["name"], show_lines=True, box=box.HEAVY_EDGE)
    table.add_column("Name")
    table.add_column("Description")
    for key, value in index.items():
        if not value or key == "url":
            continue
        key = key.replace("_", " ")
        value = make_renderable(value)
        table.add_row(key.title(), value)
    print(table)


def main() -> int:
    """query the endpoint with given arguments"""
    args = get_args()
    endpoint: str = args[0]
    check_endpoint(endpoint)
    # TODO add support for items in SECONDARIES having optional third/fourth args
    try:
        index: str = args[1]
        print_index(query_api(endpoint, index))
    except IndexError:
        print_index_options(query_api(endpoint), endpoint)
    return 0


# TODO find a way to print dictionaries as a string
def make_renderable(word: Any) -> str:
    """change a variable to a renderable format"""
    if isinstance(word, (bool, int, str)):
        pass
    elif isinstance(word, list):
        if check_types(word, str):
            word = " ".join(str(v) for v in word)
        elif check_types(word, dict):
            word = str(word)
    elif isinstance(word, dict):
        word = str(word)
        # word = url_to_command(word["name"], word["url"])
    return str(word)


def url_to_command(name: str, url: str) -> str:
    """change an API response url to a string that matches dnfo's cli syntax"""
    access_point: str = url[5:].replace("/", " ")
    string: str = f"{name}: `dnfo_lite.py {access_point}`"
    return string


def make_singular(word: str) -> str:
    """get the singular form of a word"""
    if word[-3:] == "ies":
        word = word.replace("ies", "y")
    else:
        word = word.removesuffix("s")
    return word.replace("-", " ")


def check_types(list_: list, type_: Any) -> bool:
    """check to see if every item in a list matches the given type"""
    for value in list_:
        if not isinstance(value, type_):
            return False
    return True


def usage(exit_code=0):
    """help/usage section"""
    help_msg: str = """usage: dnfo_lite.py \\[endpoint] \\[index]

optional arguments:
\t-h, --help    \tshow this help and exit
\t-v, --version\tprint version information
    """
    print(help_msg)
    # TODO put these in a rich.table
    print(Panel(Columns(ENDPOINTS, expand=True), title="Available endpoints:"))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

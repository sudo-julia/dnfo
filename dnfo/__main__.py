# -*- coding: utf-8 -*-
"""display info from the Dnd 5th edition API"""
from __future__ import annotations
import sys
from typing import Any
from rich import box, print
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from dnfo import ENDPOINTS, SECONDARIES, __version__, remove_suffix
from dnfo.queries import query_database, query_website
from dnfo.database_ops.build import populate_db
from dnfo.database_ops.clear import clear_db


def get_args():
    """get arguments with sys.argv
    argument format is: location: (local, web), endpoint, index
    """
    args: list = sys.argv[1:]
    if not args:
        usage()
    args = handle_args(args)
    return args


def handle_args(args: list) -> list:
    """handle arguments"""
    # TODO config file that sets default for local or web if neither are given as args
    arg_set: set = set(args)
    help_set: set[str] = set(["-h", "--help"])
    ver_set: set[str] = set(["-v", "--version"])

    if arg_set & ver_set:
        print(f"[white]dnfo v{__version__}")
        sys.exit()
    if arg_set & help_set:
        usage()
    elif "--rebuild" in arg_set:
        sys.exit(populate_db(rebuild=True))
    elif "--build" in arg_set:
        sys.exit(populate_db())
    elif "--clear" in arg_set:
        sys.exit(clear_db())
    # TODO fix this while accounting for --local|web
    elif len(args) > 5 and args[0] not in SECONDARIES:
        print(f"{args[0]} only supports one index as an argument.")
        usage(1)

    # TODO handle this better (maybe use a dict)
    if "--local" in arg_set:
        args.remove("--local")
        args.insert(0, "--local")
    else:
        if "--web" in args:
            args.remove("--web")
        args.insert(0, "--web")
    return args


def print_panel(columns, title=None):
    """print a rich"""
    print(Panel(Columns(columns, expand=True), title=title))


def check_endpoint(endpoint: str):
    """check if the endpoint given is valid"""
    if endpoint not in ENDPOINTS:
        print("Invalid endpoint! Options are:")
        print_panel(ENDPOINTS)
        sys.exit(1)


def print_index_options(response: list[dict[str, Any]], endpoint: str):
    """print available indexes for a given endpoint"""
    index_options: list[str] = []
    for item, _ in enumerate(response):
        index_options.append(response[item]["index"])
    del response
    print_panel(index_options, f"Available indexes for {endpoint}:")
    print(
        f"Run 'dnfo {endpoint} \\[index]' to get info on a {make_singular(endpoint)}!"
    )


def print_index(index: dict[str, Any]):
    """format the information of a dictionary to a rich Table and print"""
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
        word = remove_suffix(word, "s")
    return word.replace("-", " ")


def check_types(list_: list, type_: Any) -> bool:
    """check to see if every item in a list matches the given type"""
    for value in list_:
        if not isinstance(value, type_):
            return False
    return True


def usage(exit_code=0):
    """help/usage section"""
    help_msg: str = """usage: dnfo \\[endpoint] \\[index]

optional arguments:
\t-h, --help   \tshow this help and exit
\t-v, --version\tprint version information
\t--local      \tuse a local database
\t--web        \tuse the database located at dnd5eapi.co

database operations:
\t--build      \tpopulate the database
\t--clear      \tclear the database
\t--rebuild    \trebuild the database
    """
    print(help_msg)
    print(Panel(Columns(ENDPOINTS, expand=True), title="Available endpoints:"))
    sys.exit(exit_code)


def main() -> int:
    """query the endpoint with given arguments"""
    args = get_args()
    location: str = args.pop(0).casefold()
    try:
        endpoint: str = args.pop(0).casefold()
        check_endpoint(endpoint)
    except IndexError:
        usage()
    # TODO add support for items in SECONDARIES having optional third/fourth args
    try:
        index: str = args.pop()
        if location == "--web":
            query = query_website(endpoint, index)
        else:
            query = query_database(endpoint, index)
        print_index(query)  # type: ignore
    except IndexError:
        if location == "web":
            query = query_website(endpoint)
        else:
            query = query_database(endpoint)
        print_index_options(query_website(endpoint), endpoint)
    return 0


if __name__ == "__main__":
    main()

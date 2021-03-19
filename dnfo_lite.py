"""lite version of dnfo"""
from __future__ import annotations
import json
import sys
from typing import TypedDict
import requests
from rich import print
from rich.columns import Columns
from rich.panel import Panel

BASE_URL: str = "https://www.dnd5eapi.co/api"
ENDPOINTS: tuple = (
    "ability-scores",
    "skills",
    "proficiencies",
    "languages",
    "alignment",
    "backgrounds",
    "classes",
    "subclasses",
    "features",
    "starting-equipment",
    "races",
    "subraces",
    "traits",
    "equipment-categories",
    "equipment",
    "magic-items",
    "weapon-properties",
    "spells",
    "monsters",
    "conditions",
    "damage-types",
    "magic-schools",
    "rules",
    "rule-sections",
)
VERSION: str = "0.1.0"


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
    if len(sys.argv) == 1 or ["-h", "--help", "help"] in sys.argv:
        usage()
    elif ["-v", "--version"] in sys.argv:
        print(f"dnfo_lite v{VERSION}")
        sys.exit()
    elif len(sys.argv) > 3:
        print("For the time being, only one endpoint and one index is supported.")
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


def print_index(index: dict):
    """print information on an index"""
    print(json.dumps(index, indent=1, separators=(",", ":")))


def main() -> int:
    """main"""
    args = get_args()
    endpoint: str = args[0]
    check_endpoint(endpoint)
    try:
        index: str = args[1]
        print_index(query_api(endpoint, index))
    except IndexError:
        print_index_options(query_api(endpoint), endpoint)
    return 0


def make_singular(word: str) -> str:
    """get the singular form of a word"""
    if word[-3:] == "ies":
        word = word.replace("ies", "y")
    else:
        word = word.removesuffix("s")
    return word.replace("-", " ")


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

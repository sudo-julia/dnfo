"""lite version of dnfo"""
from __future__ import annotations
import json
import sys
from typing import TypedDict
import requests
from rich.columns import Columns
import rich

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


# pylint: disable=R0903
# TODO update this with some optionals for the different index types
class EndpointResponse(TypedDict):
    """dictionary typing for the response of any endpoint"""

    count: int
    results: list[dict[str, str]]


def check_endpoint(endpoint: str):
    """check if the endpoint given is valid"""
    if endpoint.casefold() not in ENDPOINTS:
        print("Invalid endpoint! Options are:")
        rich.print(Columns(ENDPOINTS, expand=True))
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
    rich.print(Columns(index_options, expand=True))
    print(f"Run 'dnfo {endpoint} [index]' to get info on a {get_singular(endpoint)}!")


def print_index(index: dict):
    """print information on an index"""
    print(json.dumps(index, indent=1, separators=(",", ":")))


def get_args():
    """get arguments with sys.argv
    argument format is: endpoint, index
    """
    if len(sys.argv) == 1 or ["-h", "--help", "help"] in sys.argv:
        usage()
    if len(sys.argv) > 3:
        print("For the time being, only one endpoint and one index is supported.")
        usage(1)
    args: list[str] = sys.argv[1:]
    return args


def get_singular(word: str) -> str:
    """get the singular form of a word"""
    if word[-3:] == "ies":
        word = word.replace("ies", "y")
    elif word[-2:] == "es":
        word = word.removesuffix("es")
    else:
        word = word.removesuffix("s")
    return word.replace("-", " ")


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


def usage(exit_code=0):
    """help/usage section"""
    print("usage: dnfo_lite [endpoint] [index]")
    print("To find available indexes on an endpoint, type dnfo [endpoint], ", end="")
    print("with available endpoints being:")
    # TODO put these in a rich.table
    rich.print(Columns(ENDPOINTS, expand=True))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

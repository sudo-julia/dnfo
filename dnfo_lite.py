"""lite version of dnfo"""
from __future__ import annotations
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


class EndpointResponse(TypedDict):
    """dictionary typing for the response of any endpoint"""

    count: int
    results: list[dict[str, str]]


def main() -> int:
    """main"""
    args = get_args()
    endpoint: str = args[0]
    check_endpoint(endpoint)
    try:
        index: str = args[1]
    except IndexError:
        print_indexes(query_endpoint(endpoint), endpoint)
        return 0
    print(index)
    return 0


def check_endpoint(endpoint: str):
    """check if the endpoint given is valid"""
    if endpoint.casefold() not in ENDPOINTS:
        print("Invalid endpoint! Options are:")
        rich.print(Columns(ENDPOINTS, expand=True))
        sys.exit(1)


def query_endpoint(endpoint: str) -> EndpointResponse:
    """query an endpoint for its available indexes"""
    url: str = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Invalid endpoint! Options are:")
        rich.print(Columns(ENDPOINTS, expand=True))
        sys.exit(1)
    response = response.json()
    return response


def print_indexes(response: EndpointResponse, endpoint: str):
    """:"""
    index_options: list[str] = []
    for name in range(response["count"]):
        index_options.append(response["results"][name]["index"])
    print(f"Possible options for {endpoint}:")
    rich.print(Columns(index_options, expand=True))
    print(f"Run 'dnfo [{endpoint}] [index]' to get info on an index!")


def get_args():
    """get arguments with sys.argv
    argument format is: endpoint, index
    """
    if len(sys.argv) == 1 or ["-h", "--help"] in sys.argv:
        usage(1)
    args: list[str] = sys.argv[1:]
    return args


def usage(exit_code=0):
    """help/usage section"""
    print("help, usage:")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

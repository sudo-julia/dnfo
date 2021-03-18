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
    "weapon-properties" "spells",
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
    if len(args) == 2:
        pass
    elif len(args) == 1 and args[0] not in ["-h", "--help"]:
        print_indexes(query_endpoint(args[0]), args[0])
    else:
        print("help/usage section")
        sys.exit(1)
    return 0


def query_endpoint(endpoint: str) -> EndpointResponse:
    """query an endpoint for its available indexes"""
    url: str = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Invalid endpoint!")
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
    args: list[str] = sys.argv[1:]
    return args


def usage():
    """help/usage section"""
    print("help, usage:")


if __name__ == "__main__":
    main()

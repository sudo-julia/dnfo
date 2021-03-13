"""entry point for the whole application"""
from __future__ import annotations
import argparse
import shutil
import textwrap
import requests

base_url: str = "https://www.dnd5eapi.co/api"


def get_term_columns() -> int:
    """get the terminal width. used to fit text to the screen"""
    return shutil.get_terminal_size().columns


def query_api(query: str) -> tuple[int, list[dict[str, str]]]:
    """search the API with a given query
    return the number of results and a list containing the results
    """
    response: dict = requests.get(f"{base_url}/{query}").json()
    count: int = response["count"]
    results: list[dict[str, str]] = response["results"]
    return count, results


def parse_json(count: int, results: list):
    """parse the API response"""
    for result in range(count):
        print(results[result]["name"])


def print_results(results: list):
    """print all search results"""
    width = get_term_columns()
    for line in " ".join(results).splitlines(True):
        # TODO find a way to keep words intact
        print(*textwrap.wrap(line, width), sep="\n")


def main():
    """main"""
    ...


if __name__ == "__main__":
    main()

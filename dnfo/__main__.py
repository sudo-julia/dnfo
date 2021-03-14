"""entry point for the whole application"""
from __future__ import annotations
import argparse
import requests
import rich
from rich.columns import Columns

base_url: str = "https://www.dnd5eapi.co/api"


def query_api(query: str) -> tuple[int, list[dict[str, str]]]:
    """search the API with a given query
    return the number of results and a list containing the results
    """
    response: dict = requests.get(f"{base_url}/{query}").json()
    count: int = response["count"]
    results: list[dict[str, str]] = response["results"]
    return count, results


def print_options(results: list):
    """get the names of all results for a searched field"""
    rich.print(Columns(results, expand=True))


def get_arguments() -> argparse.Namespace:
    """get the arguments"""
    parser = argparse.ArgumentParser()
    categories = parser.add_mutually_exclusive_group()
    categories.add_argument_group("spells")

    return parser.parse_args()


def main():
    """main"""
    ...


if __name__ == "__main__":
    main()

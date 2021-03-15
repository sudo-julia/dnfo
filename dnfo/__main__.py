"""entry point for the whole application"""
from __future__ import annotations
import rich
from rich.columns import Columns
from dnfo.dnfo_args import get_arguments
from dnfo.query_api import query_endpoint, query_index


def print_options(results: list[str]):
    """get the names of all results for a searched field"""
    rich.print(Columns(results, expand=True))


def main() -> int:
    """main"""
    args = get_arguments()
    print(args)
    results = query_endpoint("spells")  # type: ignore
    result_names: list[str] = []
    for name in range(results["count"]):
        result_names.append(results["results"][name]["index"])
    print_options(result_names)
    for name in range(5):
        spell_name = results["results"][name]["index"]
        # x = query_endpoint(f"spells/{results['results'][name]['index']}")
        print(query_index("spells", spell_name).text)
        # print(x.text)
    return 0


if __name__ == "__main__":
    main()

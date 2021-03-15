"""entry point for the whole application"""
from __future__ import annotations
import argparse
import rich
from rich.columns import Columns


def print_options(results: list):
    """get the names of all results for a searched field"""
    rich.print(Columns(results, expand=True))


def get_arguments() -> argparse.Namespace:
    """get the arguments"""
    # TODO subparsers, bitch
    parser = argparse.ArgumentParser()
    categories = parser.add_mutually_exclusive_group(required=True)

    # char data
    categories.add_argument("ability_score")
    categories.add_argument("skill")
    categories.add_argument("proficiencie")
    categories.add_argument("language")
    categories.add_argument("alignment")
    # backgrounds
    categories.add_argument("background")
    # classes
    categories.add_argument("class")
    categories.add_argument("subclass")
    categories.add_argument("feature")
    categories.add_argument("starting_equipment")
    # races
    categories.add_argument("race")
    categories.add_argument("subrace")
    categories.add_argument("trait")
    # equipment
    categories.add_argument("equipment")
    categories.add_argument("weapon")
    categories.add_argument("armor")
    categories.add_argument("gear")
    categories.add_argument("pack")
    categories.add_argument("magic_item")
    categories.add_argument("weapon_properties")
    # spells
    categories.add_argument("spells")
    # monsters
    categories.add_argument("monster")
    # game mechanics
    categories.add_argument("mechanic")
    categories.add_argument("condition")
    categories.add_argument("damage")
    categories.add_argument("magic_school")
    # rules
    categories.add_argument("rule")
    categories.add_argument("rule_section")

    return parser.parse_args()


def main():
    """main"""
    ...


if __name__ == "__main__":
    main()

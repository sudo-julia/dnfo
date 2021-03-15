"""get arguments for the main program"""
import argparse


def get_arguments() -> argparse.Namespace:
    """get the arguments"""
    # TODO subparsers, bitch
    # TODO custom help/usage sections
    parser = argparse.ArgumentParser()
    categories = parser.add_argument_group()

    # char data
    categories.add_argument(
        "ability_scores", help="list available ability scores", action="store_true"
    )
    categories.add_argument("skills", help="list available skills", action="store_true")
    categories.add_argument(
        "proficiencies", help="list available proficiencies", action="store_true"
    )
    categories.add_argument(
        "languages", help="list available languages", action="store_true"
    )
    categories.add_argument(
        "alignments", help="list available alignments", action="store_true"
    )
    # backgrounds
    categories.add_argument(
        "backgrounds", help="list available backgrounds", action="store_true"
    )
    # classes
    categories.add_argument(
        "classes", help="list available classes", action="store_true"
    )
    categories.add_argument(
        "subclasses", help="list available subclasses", action="store_true"
    )
    categories.add_argument(
        "features", help="list available features", action="store_true"
    )
    categories.add_argument(
        "starting_equipment",
        help="list available starting_equipment",
        action="store_true",
    )
    # races
    categories.add_argument("races", help="list available races", action="store_true")
    categories.add_argument(
        "subraces", help="list available subraces", action="store_true"
    )
    categories.add_argument("traits", help="list available traits", action="store_true")
    # equipment
    categories.add_argument(
        "equipment", help="list available equipment", action="store_true"
    )
    categories.add_argument(
        "weapons", help="list available weapons", action="store_true"
    )
    categories.add_argument("armor", help="list available armor", action="store_true")
    categories.add_argument("gear", help="list available gear", action="store_true")
    categories.add_argument("packs", help="list available packs", action="store_true")
    categories.add_argument(
        "magic_items", help="list available magic_items", action="store_true"
    )
    categories.add_argument(
        "weapon_properties",
        help="list available weapon_properties",
        action="store_true",
    )
    # spells
    categories.add_argument("spells", help="list available spells", action="store_true")
    # monsters
    categories.add_argument(
        "monsters", help="list available monsters", action="store_true"
    )
    # game mechanics
    categories.add_argument(
        "mechanics", help="list available mechanics", action="store_true"
    )
    categories.add_argument(
        "conditions", help="list available conditions", action="store_true"
    )
    categories.add_argument(
        "damages", help="list available damages", action="store_true"
    )
    categories.add_argument(
        "magic_schools", help="list available magic_schools", action="store_true"
    )
    # rules
    categories.add_argument("rules", help="list available rules", action="store_true")
    categories.add_argument(
        "rule_sections", help="list available rule_sections", action="store_true"
    )

    return parser.parse_args()

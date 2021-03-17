"""get arguments for the main program"""
import argparse


def get_arguments() -> argparse.Namespace:
    """get the arguments"""
    # TODO custom help/usage sections
    # TODO if arg is given with no positional, pull up options
    #      else, search for the given arg
    parser = argparse.ArgumentParser()
    categories = parser.add_argument_group()

    # char data
    categories.add_argument(
        "-a",
        "--ability_scores",
        help="list available ability scores",
        action="store_false",
    )
    categories.add_argument(
        "-k", "--skills", help="list available skills", action="store_false"
    )
    categories.add_argument(
        "-p",
        "--proficiencies",
        help="list available proficiencies",
        action="store_false",
    )
    categories.add_argument(
        "-l", "--languages", help="list available languages", action="store_false"
    )
    categories.add_argument(
        "--alignments", help="list available alignments", action="store_false"
    )
    # backgrounds
    categories.add_argument(
        "-b", "--backgrounds", help="list available backgrounds", action="store_false"
    )
    # classes
    categories.add_argument(
        "-c", "--classes", help="list available classes", action="store_false"
    )
    categories.add_argument(
        "-u", "--subclasses", help="list available subclasses", action="store_false"
    )
    categories.add_argument(
        "-f", "--features", help="list available features", action="store_false"
    )
    categories.add_argument(
        "-q",
        "--starting_equipment",
        help="list available starting_equipment",
        action="store_false",
    )
    # races
    categories.add_argument(
        "--races", help="list available races", action="store_false"
    )
    categories.add_argument(
        "--subraces", help="list available subraces", action="store_false"
    )
    categories.add_argument(
        "-t", "--traits", help="list available traits", action="store_false"
    )
    # equipment
    categories.add_argument(
        "-e", "--equipment", help="list available equipment", action="store_false"
    )
    categories.add_argument(
        "-w", "--weapons", help="list available weapons", action="store_false"
    )
    categories.add_argument(
        "--armor", help="list available armor", action="store_false"
    )
    categories.add_argument(
        "-g", "-gear", help="list available gear", action="store_false"
    )
    categories.add_argument(
        "--packs", help="list available packs", action="store_false"
    )
    categories.add_argument(
        "--magic_items", help="list available magic_items", action="store_false"
    )
    categories.add_argument(
        "--weapon_properties",
        help="list available weapon_properties",
        action="store_false",
    )
    # spells
    categories.add_argument(
        "-s",
        "--spells",
        nargs="?",
        const="list",
        help="""without an argument, list all available spells.
                            otherwise, display spell info""",
        type=str,
        metavar="SPELL",
    )
    # monsters
    categories.add_argument(
        "-m", "--monsters", help="list available monsters", action="store_false"
    )
    # game mechanics
    categories.add_argument(
        "-o", "--conditions", help="list available conditions", action="store_false"
    )
    categories.add_argument(
        "-d", "--damages", help="list available damages", action="store_false"
    )
    categories.add_argument(
        "--magic_schools",
        help="list available magic_schools",
        action="store_false",
    )
    # rules
    categories.add_argument(
        "-r", "--rules", help="list available rules", action="store_false"
    )
    categories.add_argument(
        "--rule_sections", help="list available rule_sections", action="store_false"
    )

    return parser.parse_args()

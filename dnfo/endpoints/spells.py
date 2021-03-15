"""format a spell for the commandline"""
from __future__ import annotations
from rich.console import Console
from rich.table import Table


def print_spell(spell: dict):
    """print a formatted spell"""
    display = Table(title=spell["name"], show_lines=True)

    display.add_column("Description", justify="center", no_wrap=True)

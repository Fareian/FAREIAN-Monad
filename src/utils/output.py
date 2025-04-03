import os
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
from typing import List
import questionary
from questionary import Style as QuestionaryStyle
import asyncio
import sys


def show_logo():
    """Clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def show_dev_info():
    """Displays version information"""
    console = Console()
    table = Table(
        show_header=False,
        box=box.DOUBLE,
        border_style="bright_cyan",
        pad_edge=False,
        width=85,
        highlight=True,
    )
    table.add_column("Content", style="bright_cyan", justify="center")
    table.add_row("✨ FAREIAN Monad Bot 1.8 ✨")
    table.add_row("─" * 43)
    table.add_row("")
    print("   ", end="")
    print()
    console.print(table)
    print()


async def show_menu(title: str, options: List[str]) -> str:
    """Displays an interactive menu with the given options and returns the selected option."""
    try:
        print("\n")
        custom_style = QuestionaryStyle([
            ("question", "fg:#B8860B bold"),
            ("answer", "fg:#ffffff bold"),
            ("pointer", "fg:#B8860B bold"),
            ("highlighted", "fg:#B8860B bold"),
            ("instruction", "fg:#666666"),
        ])
        print()
        result = await questionary.select(
            title,
            choices=options,
            style=custom_style,
            qmark="🎯",
            instruction="(Use arrow keys and Enter to select)",
        ).ask_async()
        return result
    except KeyboardInterrupt:
        print("\n\nExiting program... Goodbye! 👋")
        sys.exit(0)

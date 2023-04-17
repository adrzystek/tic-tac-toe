import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState


class ConsoleRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        clear_screen()
        if game_state.winner:
            print_blinking(game_state.grid.cells, game_state.winning_cells)
            print(f"{game_state.winner} wins \N{party popper}")
        else:
            print_solid(game_state.grid.cells)
            if game_state.tie:
                print("No one wins this time \N{neutral face}")


def clear_screen() -> None:
    print("\033c", end="")


def blink(text: str) -> str:
    return f"\033[5m{text}\033[0m"


def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)


def print_solid(cells: Iterable[str]) -> None:
    grid_template = (
        "    A   B   C\n"
        "   -----------\n"
        "1 ┆ {0} │ {1} │ {2}\n"
        "  ┆───┼───┼───\n"
        "2 ┆ {3} │ {4} │ {5}\n"
        "  ┆───┼───┼───\n"
        "3 ┆ {6} │ {7} │ {8}\n"
    )
    print(textwrap.dedent(grid_template).format(*cells))

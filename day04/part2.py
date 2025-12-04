from __future__ import annotations

import os.path
from itertools import product

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Grid:
    def __init__(self, inp: str) -> None:
        self.inp = inp
        self.grid = self._load_grid()
        self.max_x = len(inp[0])
        self.max_y = len(inp.splitlines())

    def _load_grid(self) -> dict[tuple[int, int], str]:
        grid = dict()
        for y, l in enumerate(self.inp.splitlines()):
            for x, m in enumerate(l):
                if m == '@':
                    grid[(y, x)] = m
        return grid


def count_rolls_of_paper(grid: dict[tuple[int, int], str]) -> int:
    d = [0, 1, -1]
    remove = []

    for tup in grid:
        count = 0
        x, y = tup
        for dx, dy in product(d, d):
            if (dx == 0) and (dy == 0):
                continue
            if (x + dx, y + dy) in grid:
                count += 1
        if count < 4:
            remove.append((x, y))

    if len(remove) == 0:
        return 0

    for rem in remove:
        del grid[rem]

    return len(remove) + count_rolls_of_paper(grid)


def _solve(inp: str) -> int:
    grid = Grid(inp).grid
    return count_rolls_of_paper(grid)


_TESTS = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
_EXPECTED = 43


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    (
        (_TESTS, _EXPECTED),
    ),
)
def test(input_str: str, expected: int) -> None:
    assert _solve(input_str) == expected


def main() -> int:
    with open(_INPUT) as fp:
        print(_solve(fp.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

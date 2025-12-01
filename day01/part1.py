from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    dial = 50
    result = 0
    for line in inp.splitlines():
        d, n = line[0], int(line[1:])
        if d == 'L':
            dial -= n
        elif d == 'R':
            dial += n
        dial %= 100
        if dial == 0:
            result += 1

    return result


_TESTS = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
_EXPECTED = 3


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

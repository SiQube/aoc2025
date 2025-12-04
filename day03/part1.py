from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    joltages = []
    for bank in inp.splitlines():
        joltage_1 = 0
        jolt_id = 0
        joltage_2 = 0
        for idx, bat_s in enumerate(bank[:-1]):
            bat = int(bat_s)
            if bat > joltage_1:
                joltage_1 = bat
                jolt_id = idx

        for idx, bat_s in enumerate(bank[jolt_id+1:]):
            bat = int(bat_s)
            if bat > joltage_2:
                joltage_2 = bat

        joltages.append(int(str(joltage_1)+str(joltage_2)))
    return sum(joltages)


_TESTS = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""
_EXPECTED = 357


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

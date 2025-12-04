from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def jolt_bank(bank: str) -> int:
    max_len = len(bank) - 12
    index = 0
    ret: list[str] = []
    while len(ret) < 12:
        bb = bank[index:max_len+1]
        index += bb.index(max(bb))
        if max_len == index:
            ret.append(bank[index:])
            break
        ret.append(bank[index])
        index += 1
        max_len += 1

    return int(''.join(ret))


def _solve(inp: str) -> int:
    joltages = []
    for bank in inp.splitlines():
        joltages.append(jolt_bank(bank))

    return sum(joltages)


_TESTS = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""
_EXPECTED = 3121910778619


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

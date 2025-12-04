from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    invalid = []
    for line in inp.split(','):
        s, e = line.split('-')
        for num in range(int(s), int(e)+1):
            num_s = str(num)
            if len(num_s) % 2 == 1:
                continue
            first_half = num_s[:len(num_s)//2]
            second_half = num_s[len(num_s)//2:]
            if first_half == second_half:
                invalid.append(num)

    return sum(invalid)


_TESTS = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""
_EXPECTED = 1227775554


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

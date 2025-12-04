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
            num_l = len(num_s)
            for p_l in range(1, (num_l // 2) + 1):
                if num_l % p_l != 0:
                    continue
                comb = [num_s[ll*p_l:(ll+1)*p_l] for ll in range(num_l // p_l)]
                if len(set(comb)) == 1:
                    invalid.append(num)
                    break

    return sum(invalid)


_TESTS = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""
_EXPECTED = 4174379265


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

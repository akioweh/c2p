from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


def solve(N: int, joker_pos: int, q_s: Iterable[int]) -> Iterable[int]:
    q_s = iter(q_s)
    first_q = next(q_s)
    yield 2

    edges = False
    mid = True
    l, r = 1, N
    mid_l, mid_r = joker_pos, joker_pos
    if first_q == joker_pos:
        mid = False
        edges = True
    elif first_q < joker_pos:
        mid_l = joker_pos - 1
    else:
        mid_r = joker_pos + 1

    full = False
    for q in q_s:
        if full:
            yield N
            continue

        if edges:
            if q < r:
                r -= 1
            if q > l:
                l += 1
            # bounds check
            if l + 1 >= r:
                full = True
                yield N
                continue

        if not mid:  # we can yield directly
            yield l + (N + 1 - r)
            continue

        # process mid
        if q < mid_l:
            mid_l -= 1
        elif q > mid_r:
            mid_r += 1
        elif not edges:
            edges = True
        # bounds check
        if not edges:
            if mid_l == 1 and mid_r == N:
                full = True
                yield N
                continue
            yield mid_r - mid_l + 1
        else:
            # edge merge check
            if l + 1 >= mid_l:
                mid = False
                l = mid_r
            elif mid_r + 1 >= r:
                mid = False
                r = mid_l
            # we successfully merged
            if not mid:
                if l + 1 >= r:
                    full = True
                    yield N
                    continue
                yield l + (N + 1 - r)
            else:
                yield mid_r - mid_l + l + N - r + 2


T = int(input())

for _ in range(T):
    n, m, _ = read_ints()
    data = read_ints()

    for num in solve(n, m, data):
        stdout.write(f'{num} ')
    stdout.write('\n')

stdout.flush()

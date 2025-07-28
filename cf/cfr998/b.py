from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N_cows, M_deck_size = read_ints()
    hands = [
        list(read_ints())
        for _ in range(N_cows)
    ]

    if N_cows == 1:
        print('1')
        continue

    for hand in hands:
        hand.sort()

    idxs = list(range(N_cows))
    idxs.sort(key=hands.__getitem__[0])

    for i, j in enumerate(idxs):
        if hands[j][0] != i:
            print('-1')
            break
    else:
        if all(
            hands[i] == list(range(hands[i][0], M_deck_size * N_cows, N_cows))
            for i in range(N_cows)
        ):
            print(' '.join(str(x + 1) for x in idxs))
        else:
            print('-1')

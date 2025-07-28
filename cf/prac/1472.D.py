from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(read_ints())

    evens, odds = [], []
    for val in arr:
        if val % 2:
            odds.append(val)
        else:
            evens.append(val)

    odds.append(0)
    evens.append(0)
    evens.sort()
    odds.sort()

    alice, bob = 0, 0
    a_turn = True
    while evens[-1] != 0 or odds[-1] != 0:
        if a_turn:
            if evens[-1] == 0 or (odds[-1] != 0 and odds[-1] > evens[-1]):
                odds.pop()
            else:
                alice += evens.pop()
        else:
            if odds[-1] == 0 or (evens[-1] != 0 and evens[-1] > odds[-1]):
                evens.pop()
            else:
                bob += odds.pop()
        a_turn = not a_turn

    if alice == bob:
        print('Tie\n')
    elif alice > bob:
        print('Alice\n')
    else:
        print('Bob\n')

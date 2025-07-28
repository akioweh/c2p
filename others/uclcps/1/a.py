from collections import Counter
from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


T = int(input())

for _ in range(T):
    input()
    freqs = Counter(read_ints())
    print(
        sum(v // 2 for v in freqs.values())
    )

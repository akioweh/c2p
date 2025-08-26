from sys import stdin
from typing import Iterator


def read_ints() -> Iterator[int]:
    return map(int, stdin.readline().split())


T = int(input())

for _ in range(T):
    pass

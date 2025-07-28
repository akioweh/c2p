from sys import setrecursionlimit
from functools import cache


@cache
def n_ways(n: int) -> int:
    if n == 1:
        return 1
    return sum(
        n_ways(n - i_) * n_ways(i_)
        for i_ in range(n)
    )


if __name__ == '__main__':
    setrecursionlimit((1 << 16) - 1)
    print(n_ways(100))

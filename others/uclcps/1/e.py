from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


T = int(input())

for _ in range(T):
    N = int(input())
    # we set c = 1, and find coprime a, b
    c = 1
    # now we split N - 1 into a and b
    rest = N - 1
    if rest % 2:  # odd -> even + odd
        # two consecutive numbers *always* coprime
        a, b = N // 2, rest // 2
    else:  # even -> even + even OR odd + odd
        # two 2-apart numbers coprime *when they're odd*
        a, b = rest // 2 - 1, rest // 2 + 1
        if not a % 2:
            a -= 1
            b += 1

    print(a, b, c)

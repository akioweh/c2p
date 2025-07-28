from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


T = int(input())

for _ in range(T):
    K = int(input())
    if (K - 1) % 3:
        print('NO')
    else:
        print('YES')

from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


N = input()
arr = list(read_ints())

print(max(arr) - min(arr) + 1 - len(set(arr)))

from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


T = int(input())

for _ in range(T):
    a1, a2, a4, a5 = read_ints()
    option1 = a1 + a2
    # a2 + a3 = a4
    option2 = a4 - a2
    # a3 + a4 = a5
    option3 = a5 - a4
    print(4 - len({option1, option2, option3}))

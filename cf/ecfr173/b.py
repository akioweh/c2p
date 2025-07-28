T = int(input())

for _ in range(T):
    n, d = map(int, input().split())

    print(1, end=' ')

    if n >= 3 or d % 3 == 0:
        print(3, end=' ')

    if d == 0 or d == 5:
        print(5, end=' ')

    if n >= 3 or d == 7:
        print(7, end=' ')

    if n >= 6 or d == 9 or (n >= 3 and d % 3 == 0):
        print(9, end=' ')

    print()

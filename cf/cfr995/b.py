T = int(input())

for _ in range(T):
    n, a, b, c = list(map(int, input().split()))

    dist_3d = a + b + c

    cycles, remainder = divmod(n, dist_3d)
    if not remainder:
        print(cycles * 3)
        continue

    if a >= remainder:
        print(cycles * 3 + 1)
    elif a + b >= remainder:  # a + b > remainder
        print(cycles * 3 + 2)
    else:
        print(cycles * 3 + 3)

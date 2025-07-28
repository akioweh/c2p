T = int(input())

for _ in range(T):
    n = int(input())

    exp = 0
    while n > 3:
        n //= 4
        exp += 1

    print(2**exp)

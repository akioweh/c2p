T = int(input())

for _ in range(T):
    N = int(input())
    a_s = list(map(int, input().split()))
    b_s = list(map(int, input().split()))

    gains = [
        a_s[i] - b_s[i + 1]
        for i in range(N - 1)
    ]
    gains.append(a_s[-1])

    print(sum(filter(lambda x: x > 0, gains)))

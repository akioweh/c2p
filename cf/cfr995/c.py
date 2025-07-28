T = int(input())

for _ in range(T):
    N, M, K = list(map(int, input().split()))
    a_s = list(map(int, input().split()))
    q_s = set(map(int, input().split()))

    n_q = len(q_s)
    if n_q == N:
        print('1' * M)
    elif n_q == N - 1:
        all_qs = set(range(1, N + 1))
        missing = all_qs - q_s
        assert len(missing) == 1
        missing = missing.pop()
        for i in a_s:
            print('1' if missing == i else '0', end='')
        print()
    else:
        print('0' * M)

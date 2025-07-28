T = int(input())

for _ in range(T):
    # given N, find a sequence A of N integers that:
    # 1 <= A[i] <= N
    # number of longest palindromic subsequences > N

    N = int(input())

    res = [1, 1] + list(range(2, N - 1)) + [1]

    print(' '.join(map(str, res)))

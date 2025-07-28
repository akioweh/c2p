N, K = map(int, input().split())

n_ways = [1] * N
for _ in range(K - 1):
    next_ways = [0] * N
    for n, ways in enumerate(n_ways):
        for next_n in range(n, N, n + 1):
            next_ways[next_n] += ways
    n_ways = next_ways

print(sum(n_ways) % 1_000_000_007)

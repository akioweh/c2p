from sys import stdin, stdout

# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints():
    return map(int, input().split())


T = int(input())

for _ in range(T):
    n, k = read_ints()

    res = 0
    segment_length = n
    mid = n + 1
    n_segments = 1
    while segment_length >= k:
        if segment_length % 2:
            res += n_segments * mid
        segment_length //= 2
        n_segments *= 2
    res //= 2

    print(f'{res}\n')

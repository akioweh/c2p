from collections import defaultdict
from bisect import bisect_right
from sys import stdin, stdout

# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints():
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    l, r = [], []
    must_have = defaultdict(list)
    for i in range(N):
        l_, r_ = read_ints()
        l.append(l_)
        r.append(r_)
        if l_ == r_:
            must_have[l_].append(i)

    filled_start = []
    filled_end = []
    filled = sorted(must_have.keys())
    prev = -2
    cur_filled = False
    for f in filled:
        if not cur_filled:
            filled_start.append(f)
            cur_filled = True
        elif f != prev + 1:
            filled_end.append(prev)
            filled_start.append(f)
        prev = f
    if cur_filled:
        filled_end.append(prev)

    f_max = len(filled_start)

    for i in range(N):
        if l[i] == r[i]:
            if len(must_have[l[i]]) > 1:
                print('0')
            else:
                print('1')
        else:
            idx = bisect_right(filled_start, l[i]) - 1
            if idx != -1 and filled_end[idx] >= r[i]:
                print('0')
            else:
                print('1')
    print('\n')

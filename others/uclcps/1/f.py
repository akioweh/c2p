from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())


N = int(input())
pos = list(read_ints())
vel = list(read_ints())


def possible(_t):
    intervals = [
        (start - vel_ * _t, start + vel_ * _t)
        for start, vel_ in zip(pos, vel)
    ]
    # see if all intervals overlap at any point (standard algorithm)
    intervals.sort()
    it = iter(intervals)
    cur_min, cur_max = next(it)
    for start, end in it:
        if start > cur_max:
            return False
        cur_min = max(cur_min, start)
        cur_max = min(cur_max, end)
        if cur_min > cur_max:
            return False
    return True


L = max(pos) - min(pos)
min_vel = min(vel)
# binary search on answer space
min_t, max_t = 0., L / min_vel
for _ in range(60):  # precision has log relationship with iterations
    mid_t = (min_t + max_t) / 2
    if possible(mid_t):
        max_t = mid_t
    else:
        min_t = mid_t

print(max_t)

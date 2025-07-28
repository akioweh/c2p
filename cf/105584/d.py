from bisect import bisect_right, bisect_left
from collections import defaultdict
from typing import Iterable


def read_ints() -> Iterable[int]:
    return map(int, input().split())


def find_next(arr, val):
    i = bisect_right(arr, val)
    if i != len(arr):
        return arr[i]
    return None


def find_prev(arr, val):
    i = bisect_left(arr, val)
    if i:
        return arr[i-1]
    return None


prev_states = {}
while True:
    N_obs = int(input())
    if N_obs == 0:
        break
    x, y, D = read_ints()
    rows = defaultdict(list)
    cols = defaultdict(list)
    for _ in range(N_obs):
        x_, y_ = read_ints()
        rows[y_].append(x_)
        cols[x_].append(y_)

    for r in rows:
        rows[r].sort()
    for c in cols:
        cols[c].sort()

    dirs = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )

    cur_dir = 0

    while True:
        state = (x, y, cur_dir)
        if state in prev_states:
            prev_D = prev_states[state]
            cycle_len = prev_D - D
            assert cycle_len > 0
            D %= cycle_len
            del prev_states[state]
        else:
            prev_states[state] = D

        if cur_dir == 0 or cur_dir == 2:
            obs_los = rows[y]
        else:
            obs_los = cols[x]

        if not obs_los:
            break

        if cur_dir == 0:  # right
            next_obs = find_next(obs_los, x)
            cur_v = x
        elif cur_dir == 1:  # up
            next_obs = find_next(obs_los, y)
            cur_v = y
        elif cur_dir == 2:  # left
            next_obs = find_prev(obs_los, x)
            cur_v = x
        else:  # down
            next_obs = find_prev(obs_los, y)
            cur_v = y

        if next_obs is None:
            break

        dd = abs(cur_v - next_obs) - 1
        if dd >= D:
            break

        D -= dd
        x += dirs[cur_dir][0] * dd
        y += dirs[cur_dir][1] * dd

        cur_dir += 1
        cur_dir %= 4

    if D:
        x += dirs[cur_dir][0] * D
        y += dirs[cur_dir][1] * D

    print(x, y)
    prev_states.clear()


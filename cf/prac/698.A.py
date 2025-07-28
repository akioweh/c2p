n = int(input())
arr = list(map(int, input().split()))

# v -> gym | contest
# 0 ->  0  |  0
# 1 ->  0  |  1
# 2 ->  1  |  0
# 3 ->  1  |  1

prev_day = [0, 0, 0]
for i, v in enumerate(arr):
    prev_day[:] = (
        max(prev_day),
        max(prev_day[0], prev_day[2]) + 1 if v & 0b10 else 0,
        max(prev_day[0], prev_day[1]) + 1 if v & 0b01 else 0
    )

print(n - max(prev_day))

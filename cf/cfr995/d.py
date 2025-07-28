from bisect import bisect_left, bisect_right


T = int(input())

for _ in range(T):
    n, min_sum, max_sum = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()

    orig_sum = sum(arr)
    min_diff = max(orig_sum - max_sum, 0)
    max_diff = orig_sum - min_sum

    if max_diff < 0:
        print(0)
        continue

    res = 0
    for i in range(n):
        # find upper and lower bound for j
        j_min = bisect_left(arr, min_diff - arr[i], lo=i + 1)
        j_max = bisect_right(arr, max_diff - arr[i], lo=i + 1)
        res += j_max - j_min

    print(res)

from bisect import bisect_left, bisect_right
from collections.abc import Iterable


def len_lis(nums: Iterable) -> int:
    """Length of the Longest Increasing Subsequence"""
    nums = iter(nums)
    res = [next(nums)]
    for v in nums:
        if v > res[-1]:
            res.append(v)
        else:
            res[bisect_left(res, v)] = v
    return len(res)


def len_lnds(nums: Iterable) -> int:
    """Length of the Longest Non-Decreasing Subsequence"""
    nums = iter(nums)
    res = [next(nums)]
    for v in nums:
        if v >= res[-1]:
            res.append(v)
        else:
            res[bisect_right(res, v)] = v
    return len(res)

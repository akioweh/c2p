#!/bin/python3

from bisect import bisect_left
import os


#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def playingWithNumbers(arr: list[int], queries: list[int]) -> list[int]:
    N = len(arr)
    arr.sort()
    idx = bisect_left(arr, 0)
    # n_negatives = idx; n_positives = N - idx

    tot_added = 0
    cur_abs_sum = sum(map(abs, arr))
    for q in queries:
        tot_added += q




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    _ar = list(map(int, input().rstrip().split()))

    __q = int(input().strip())

    _qs = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(_ar, _qs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

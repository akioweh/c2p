from array import array
from itertools import accumulate


def sum_digits(x: int) -> int:
    return sum(map(int, str(x)))


prefix_sum = array('L', accumulate(map(sum_digits, range(2 * 10 ** 5 + 1))))


T = int(input())

for _ in range(T):
    print(prefix_sum[int(input())])

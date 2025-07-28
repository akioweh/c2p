from collections import Counter
from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, K = read_ints()
    arr = list(read_ints())

    # modular arithmetic
    for i in range(N):
        arr[i] %= K

    nums = Counter(arr)

    if 0 in nums:
        print('0\n')
        continue

    if K in (2, 3, 5):  # primes
        print(f'{K - max(nums)}\n')
    elif K == 4:
        if nums[2] >= 2:
            print('0\n')
        elif nums[3] or (nums[2] and nums[1]):
            print('1\n')
        elif nums[1] >= 2:
            print('2\n')
        else:
            print('3\n')
    else:  # K should be in [2..5]
        raise ValueError

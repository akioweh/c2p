"""
60. Permutation Sequence
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = ''.join(map(str, range(1, n + 1)))

        if k == 1:
            return arr
        k -= 1

        state = list(range(n))
        n_cnt = list(range(n, 0, -1))
        while True:
            for i in reversed(range(n)):
                n_cnt[i] -= 1
                if n_cnt[i] == 0:
                    state[i:] = state[i+1:] + state[i:i+1]
                    n_cnt[i] = n - i
                else:
                    j = n_cnt[i]
                    state[i], state[-j] = state[-j], state[i]
                    k -= 1
                    if k == 0:
                        return ''.join(arr[i] for i in state)
                    break
            else:
                break

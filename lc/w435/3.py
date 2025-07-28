"""
Q3. Minimum Increments for Target Multiples in an Array
"""

class Solution:
    def minimumIncrements(self, nums: list[int], target: list[int]) -> int:
        # in an operation we can increase nums[i] by 1, for all i
        # find min no. of operations so each element in target has a multiple in nums

        N = len(nums)
        target = list(set(target))

        M = len(target)
        opss = []
        for i, t in enumerate(target):
            opss.append(
                [(t - (n % t)) % t for n in nums]
            )

        min_ops = target.copy()
        for i in range(N):
            ops_i = [opss[j][i] for j in range(M)]
            improvements = [0] * M  # if we use this i for target[j], what's the reduction in ops?
            for j in range(M):
                improvements[j] = min_ops[j] - ops_i[j]
            best_improvement = max(range(M), key=lambda j: improvements[j])
            if improvements[best_improvement] > 0:
                min_ops[best_improvement] = ops_i[best_improvement]
        return sum(min_ops)


if __name__ == '__main__':
    temp = Solution()
    print(temp.minimumIncrements([8, 4], [10, 5]))

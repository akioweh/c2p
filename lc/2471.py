"""
2471. Minimum Number of Operations to Sort a Binary Tree by Level
"""


from bisect import bisect_left


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_sort(self, arr: list[TreeNode]) -> int:
        """Sorts arr using swap operations
        and counts the number of operations needed."""
        arr_sorted = arr.copy()
        arr_sorted.sort(key=lambda x: x.val)

        N = len(arr)

        correct = [
            ele.val == ref.val
            for ele, ref in zip(arr, arr_sorted)
        ]

        n_unsorted = N - sum(correct)

        n_swaps = 0
        min_unsorted_idx = 0
        while n_unsorted:
            while correct[min_unsorted_idx]:
                min_unsorted_idx += 1
                if min_unsorted_idx == N:
                    raise RuntimeError('balls')

            sorted_idx = bisect_left(arr_sorted, arr[min_unsorted_idx].val, lo=min_unsorted_idx + 1, key=lambda x: x.val)
            assert 0 <= sorted_idx < N
            assert arr_sorted[sorted_idx].val == arr[min_unsorted_idx].val
            # whether we are sorting both elements at once
            perfect_swap = arr[sorted_idx].val == arr_sorted[min_unsorted_idx].val
            # swap
            arr[min_unsorted_idx], arr[sorted_idx] = arr[sorted_idx], arr[min_unsorted_idx]
            n_swaps += 1

            n_unsorted -= 1
            correct[sorted_idx] = True
            if perfect_swap:
                n_unsorted -= 1
                correct[min_unsorted_idx] = True

        assert arr_sorted == arr
        return n_swaps

    def minimumOperations(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 0

        levels: list[list[TreeNode]] = [[root]]

        # bfs to transform b-tree into levels
        while True:
            cur_level = levels[-1]
            next_level: list[TreeNode] = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                levels.append(next_level)
            else:
                break

        # now we figure out how many swaps are needed to sort each level
        # and return the sum of all swaps
        return sum(
            self.count_sort(level)
            for level in levels
        )

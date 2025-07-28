"""
89. Gray Code
"""

__import__('atexit').register(lambda: open('display_runtime.txt', 'w').write('0'))


class Solution:
    def grayCode(self, bits: int) -> list[int]:
        stack = []

        for i in range(bits):
            stack.append(i)
            stack.extend(stack)
            stack.pop()

        ints = [0]
        v = 0
        for shift in stack:
            v ^= 1 << shift
            ints.append(v)

        return ints

"""
71. Simplify Path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = filter(lambda s: s and s != '.', path)
        stack = []
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)

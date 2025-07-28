"""
1910. Remove All Occurrences of a Substring
"""


def lsp_(s) -> list[int]:
    res = [0]
    idx = 0
    for c in s[1:]:
        while idx and c != s[idx]:
            idx = res[idx - 1]
        if c == s[idx]:
            idx += 1
        res.append(idx)
    return res


class Solution:
    def removeOccurrences(self, s: str, p: str) -> str:
        M = len(p)
        lsp = lsp_(p)
        chr_stack = []
        idx_stack = [0]
        idx = 0
        for c in s:
            chr_stack.append(c)
            while idx and c != p[idx]:
                idx = lsp[idx - 1]
            if c == p[idx]:
                idx += 1
            idx_stack.append(idx)

            if idx == M:
                for _ in range(M):
                    chr_stack.pop()
                    idx_stack.pop()
                idx = idx_stack[-1]

        return ''.join(chr_stack)

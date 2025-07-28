"""
balls.
"""

from collections import defaultdict
from typing import Iterator, Sequence


def lsp(s: Sequence) -> list[int]:
    """``lsp(s)[i]`` is the length of
    the longest proper suffix of ``s[:i]``
    which is also a prefix of ``s[:i]``.
    """
    N = len(s)
    res = [0, 0]
    pi = 0
    for si in range(1, N):
        while pi and s[pi] != s[si]:
            pi = res[pi]
        if s[si] == s[pi]:
            pi += 1
        res.append(pi)
    return res


def dfa(s: Sequence) -> list[dict[..., int]]:
    """Constructs a DFA that accepts ``L = {w | w.endswith(s)}``.
    ``res[i][c] -> j`` is a transition from state ``i`` to state ``j`` consuming ``c``.
    State ``0`` is the start state; ``len(s)`` is the accepting state.
    In addition, the DFA is self-looping; it can be used to
    find all occurrences of ``s`` in a string.
    """
    N = len(s)
    res = [
        defaultdict(int)
        for _ in range(N + 1)
    ]
    alphabet = set(s)
    for i in range(N + 1):
        for c in alphabet:
            j = i
            while j and s[j] != c:
                j = res[j][c]
            if s[j] == c:
                j += 1
            res[i][c] = j
    for i in range(N + 1):
        for c in alphabet:
            if c not in res[i]:
                res[i][c] = res[res[i][c]][c]
    return res


def matches_lsp(s: str, p: str, _lsp: list[int]) -> Iterator[int]:
    """Yields all indices of occurrences of ``p`` in ``s``.
    KMP using suffix-prefix array.
    """
    N = len(s)
    M = len(p)
    i = j = 0
    while i < N:
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == M:
                yield i - M
                j = _lsp[j]
        else:
            if j:
                j = _lsp[j]
            else:
                i += 1


if __name__ == '__main__':
    S = 'e' * 1
    P = 'eeeeeee'
    _lsp = lsp(P)
    print(_lsp)
    _res = list(matches_lsp(S, P, _lsp))
    print(_res)
    # print(S)
    # for _i in range(len(S)):
    #     if _i in _res:
    #         print('^', end='')
    #     else:
    #         print(' ', end='')
    # print()

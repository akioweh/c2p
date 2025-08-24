"""
balls.
"""

from typing import Iterator, Sequence


def lsp[T](s: Sequence[T]) -> list[int]:
    """Computes the "suffix-prefix array" of s
    in O(|s|).

    ``lsp(s)[i]`` is the length of
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


def dfa[T](s: Sequence[T]) -> list[dict[T, int]]:
    """Constructs a DFA that accepts ``L = {w | w.endswith(s)}``
    in O(|s|*|S|) where S is the alphabet.

    ``res[i][c] -> j`` is a transition from state ``i`` to state ``j`` consuming ``c``.
    State ``0`` is the start state; ``len(s)`` is the accepting state.
    In addition, the DFA is self-looping; it can be used to
    find multiple occurrences of ``s`` in a string.
    """
    alphabet = set(s)
    res: list[dict[T, int]] = []
    cur = {c: 0 for c in alphabet}
    for i, t in enumerate(s):
        res.append(cur.copy())
        res[i][t] = i + 1
        cur = res[cur[t]]
    # looping transitions
    res.append(cur.copy())

    return res


def matches_lsp(s: str, p: str, _lsp: list[int]) -> Iterator[int]:
    """Yields all occurrences of ``p`` in ``s``
    by their starting indices in ``s``.

    KMP algorithm using a suffix-prefix array.
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


def matches_dfa(s: str, p: str, _dfa: list) -> Iterator[int]:
    """Yields all occurrences of ``p`` in ``s``
    by their starting indices in ``s``.

    KMP algorithm using a DFA.
    """
    M = len(p)
    j = 0
    for i, c in enumerate(s):
        j = _dfa[j].get(c, 0)
        if j == M:
            yield i - M + 1


if __name__ == '__main__':
    S = r'abcoingoa bcboiiinabccg a faabce fz( fa_ fj;abckla;owi-jadsfj \ak_fj e e aabczd e a_f in the rdb ininininit abcdba abcabcabcabc'
    P = 'abc'
    _lsp = lsp(P)
    print(_lsp)
    _res1 = list(matches_lsp(S, P, _lsp))
    print(_res1)
    print(S)
    for _i in range(len(S)):
        if _i in _res1:
            print('^', end='')
        else:
            print(' ', end='')
    print('\n\n')

    _dfa = dfa(P)
    for i, r in enumerate(_dfa):
        print(f'{i}  {r}')
    _res2 = list(matches_dfa(S, P, _dfa))
    print(_res2)
    print(S)
    for _i in range(len(S)):
        if _i in _res2:
            print('^', end='')
        else:
            print(' ', end='')
    print('\n')
    print(_res1 == _res2)

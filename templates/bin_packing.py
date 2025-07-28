from collections import Counter
from itertools import accumulate
from operator import mul


def pack_bins_bitmask(w: list[int], lim: int) -> int:
    """O( N * 2**N ) DP over subsets solution
    for the bin packing problem.
    """
    n = len(w)
    if n == 0:
        return 0
    if max(w) > lim:
        return -1

    dp_bins = [n + 1] * (1 << n)
    dp_fill = [0] * (1 << n)
    dp_bins[0] = 1
    for state in range(1 << n):
        for i in range(n):
            if state & (ele := 1 << i):
                continue
            if (new_fill := dp_fill[state] + w[i]) <= lim:
                cand = (dp_bins[state], new_fill)
            else:
                cand = (dp_bins[state] + 1, w[i])
            nxt = state | ele
            dp_bins[nxt], dp_fill[nxt] = min((dp_bins[nxt], dp_fill[nxt]), cand)

    return dp_bins[-1]


def pack_bins_mult(wc: Counter[int], lim: int) -> int:
    """O( len(wc) * prod(x + 1 for x in wc.values()) ) DP optimized for
    multiplicity of weights.
    """
    if not wc:
        return 0
    if max(wc) > lim:
        return -1

    ele, cnt = zip(*wc.items())
    t = len(ele)

    # state compression
    rdx = [1] + list(accumulate(map(lambda u: u + 1, cnt), func=mul))
    n = rdx[-1]

    # dp over subsets/states
    dp = [(sum(cnt) + 1, 0)] * n
    dp[0] = (1, 0)
    for state in range(n):
        n_bins, fill = dp[state]
        # de-compress state
        v = state
        s = [0] * t
        for i in reversed(range(t)):
            s[i], v = divmod(v, rdx[i])

        for k in range(t):
            if s[k] == cnt[k]:
                continue
            if fill + ele[k] <= lim:
                cand = (n_bins, fill + ele[k])
            else:
                cand = (n_bins + 1, ele[k])
            nxt = state + rdx[k]
            dp[nxt] = min(dp[nxt], cand)

    return dp[-1][0]

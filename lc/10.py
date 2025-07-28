"""
10. Regular Expression Matching
"""

class Solution:
    @staticmethod
    def fullmatch(s: str, x: str) -> bool:
        len_s, len_x = len(s), len(x)
        # "base" cases
        if not (len_s or len_x):  # both empty
            return True
        if bool(len_s) ^ bool(len_x):  # one empty
            if not len_s:  # no string
                # only valid if all that remains are 0+ matches
                return all(m == ',' or m.isupper() for m in x)
            return False  # regex exhausted

        # shrink from both ends until we reach a non-certain match
        # (when we have a 0+ match and there's 1+ possible characters to match)
        # LEFT
        l_s, l_x = 0, 0
        while l_s < len_s and l_x < len_x:
            cur_m = x[l_x]  # raw match unit
            m_var = cur_m.isupper() or cur_m == ','  # 0+ variable match?
            m_chr = cur_m.lower() if cur_m != ',' else '.'  # actual character to match
            can_match = m_chr == '.' or m_chr == s[l_s]  # can match at least 1?
            if not m_var:
                if not can_match:
                    return False  # failed single-char match
                l_s += 1
            elif can_match:  # at this point we have reached a non-certain match
                break
            # otherwise, even when it is a 0+ match, we can skip the unit if there is guaranteeded no match
            l_x += 1

        # RIGHT
        r_s, r_x = -1, -1  # it is more convenient to use negative indexing
        while l_s - r_s <= len_s and l_x - r_x <= len_x:
            cur_m = x[r_x]  # raw match unit
            m_var = cur_m.isupper() or cur_m == ','  # 0+ variable match?
            m_chr = cur_m.lower() if cur_m != ',' else '.'  # actual character to match
            can_match = m_chr == '.' or m_chr == s[r_s]  # can match at least 1?
            if not m_var:
                if not can_match:
                    return False  # failed single-char match
                r_s -= 1
            elif can_match:  # at this point we have reached a non-certain match
                break
            # otherwise, even when it is a 0+ match, we can skip the unit if there is guaranteeded no match
            r_x -= 1

        # trim s and x
        # translate to slice inexing
        r_s = None if r_s == -1 else r_s + 1
        r_x = None if r_x == -1 else r_x + 1
        s = s[l_s:r_s]
        x = x[l_x:r_x]

        if not s or not x:  # we've exhausted the string or regex; can shortcut
            return Solution.fullmatch(s, x)

        # !!! at this point, both ends start with a matchable 0+ match unit
        # so we have to brute force all possible match length combinations
        len_s, len_x = len(s), len(x)

        cur_m_l, cur_m_r = x[0], x[-1]
        max_prefix = max_suffix = len_s  # these values are the maximum chars that the 0+ units can match
        if cur_m_l != ',':
            max_prefix -= len(s.lstrip(cur_m_l.lower()))
        if cur_m_r != ',':
            max_suffix -= len(s.rstrip(cur_m_r.lower()))
        x_trim = x[1:-1]
        return any(
            Solution.fullmatch(s[_l:_r], x_trim)
            for _l in range(max_prefix + 1)
            for _r in range(len_s - max_suffix, len_s + 1)
        )

    def isMatch(self, s: str, p: str) -> bool:
        N = len(p)
        # pre-process p into a better format
        # convert x* into X
        # convert .* into ,
        # so that each "match unit" is 1 character.
        x_arr = []
        i = 0
        while i < N - 1:
            if p[i + 1] == '*':
                if p[i] == '.':
                    x_arr.append(',')
                else:
                    x_arr.append(p[i].upper())
                i += 2
            else:
                x_arr.append(p[i])
                i += 1
        # last-element
        if i < N:
            x_arr.append(p[i])

        # remove redundant consecutive identical "0+" (star) matches
        for j in range(len(x_arr) - 2, -1, -1):
            cur = x_arr[j]
            nxt = x_arr[j + 1]
            if (cur.isupper() or cur == ',') and cur == nxt:
                x_arr.pop(j + 1)

        x = ''.join(x_arr)
        return Solution.fullmatch(s, x)


class Solution2:
    def isMatch(self, text: str, pattern: str) -> bool:
        P = len(pattern)
        T = len(text)
        dp = [
            [False] * (P + 1)
            for _ in range(T + 1)
        ]

        dp[-1][-1] = True
        for i in range(T, -1, -1):
            for j in range(P - 1, -1, -1):
                first_match = i < T and pattern[j] in {text[i], '.'}
                if j + 1 < P and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


if __name__ == '__main__':
    temp = Solution2()
    print(temp.isMatch(
        'a' * 1000 + 'b' + 'a' * 1000,
        'a*' + 'aba' + 'a*'
    ))

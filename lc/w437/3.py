from operator import itemgetter


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        s_reverse = s[::-1]
        N = len(s)
        # find first and last occurences of each letter a-z
        intervals = {}
        for c_i in range(26):
            c = chr(ord('a') + c_i)
            try:
                start, end = s.index(c), N - s_reverse.index(c) - 1
                intervals[c] = (start, end)
            except ValueError:
                pass

        # we need to filter the intervals
        # for any letter in the interval, the same character must not exist outside the interval
        good_intervals = []
        for c, (start, end) in intervals.items():
            if start == 0 and end == N - 1:
                continue  # full string not allowed
            chars = set(s[start:end + 1])
            new_start = min(intervals[c_][0] for c_ in chars)
            new_end = max(intervals[c_][1] for c_ in chars)
            if not (new_start == 0 and new_end == N - 1):
                good_intervals.append((new_start, new_end))

        # find maximum number of non-overlapping intervals
        # earliest ending greedy
        good_intervals.sort(key=itemgetter(1))
        max_disjoint = 0
        last_end = -1
        for start, end in good_intervals:
            if start >= last_end:
                max_disjoint += 1
                last_end = end

        return max_disjoint >= k

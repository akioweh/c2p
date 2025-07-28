"""
30. Substring with Concatenation of All Words
"""

from itertools import chain
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n_words = len(words)
        l_word = len(words[0])
        l_subs = n_words * l_word
        l_s = len(s)
        if l_s < l_subs:
            return []
        s += '_'

        freq_diff = [0] * 26
        for char in chain(*words):
            freq_diff[ord(char) - 97] += 1
        for i in range(l_subs):
            freq_diff[ord(s[i]) - 97] -= 1

        target = Counter(words)

        ans = []
        for l in range(l_s - l_subs + 1):
            r = l + l_subs
            if not any(freq_diff):
                cur = Counter()
                for l1 in range(l, r, l_word):
                    word = s[l1:l1 + l_word]
                    if word not in target:
                        break
                    cur[word] += 1
                else:
                    if cur == target:
                        ans.append(l)
            freq_diff[ord(s[l]) - 97] += 1
            freq_diff[ord(s[r]) - 97] -= 1

        return ans


if __name__ == '__main__':
    temp = Solution()
    print(temp.findSubstring(
        "wordgoodgoodgoodbestword",
        ["word","good","best","good"]
    ))

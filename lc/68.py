"""
68. Text Justification
"""


class Solution:
    def fullJustify(self, words: list[str], max_width: int) -> list[str]:
        N = len(words)
        tot_len = sum(map(len, words))
        tot_n_words = N
        res = []
        ptr = 0
        next_word = words[ptr]
        while tot_len + tot_n_words - 1 > max_width:
            line = []
            line_n_words = 0
            line_word_chars = 0
            while line_word_chars + line_n_words + len(next_word) <= max_width:
                line.append(next_word)
                line_n_words += 1
                line_word_chars += len(next_word)
                ptr += 1
                next_word = words[ptr]

            if line_n_words > 1:
                n_space = max_width - line_word_chars
                n, e = divmod(n_space, line_n_words - 1)
                for i in range(line_n_words - 1):
                    line[i] += ' ' * n
                    if i < e:
                        line[i] += ' '
            else:
                line[0] += ' ' * (max_width - line_word_chars)
            res.append(''.join(line))
            tot_len -= line_word_chars
            tot_n_words -= line_n_words

        if tot_n_words:
            res.append(
                ' '.join(words[ptr:]) +
                ' ' * (max_width - tot_len - tot_n_words + 1)
            )

        return res

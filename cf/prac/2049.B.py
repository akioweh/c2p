from typing import Iterable


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    s = input()

    seen_p = False
    seen_s = False

    for i, c in enumerate(s):
        if c == 'p':
            if seen_s and i != N - 1:
                break
            if not seen_p:
                seen_p = True
        elif c == 's':
            if i == 0:
                continue
            if seen_p:
                break
            if not seen_s:
                seen_s = True
    else:
        print('YES')
        continue
    print('NO')

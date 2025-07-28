def gen_segments(lo, hi):
    yield [(lo, hi)]
    if lo == hi:
        return
    for mid in range(lo, hi):
        for s2 in gen_segments(mid + 1, hi):
            yield [(lo, mid)] + s2


if __name__ == '__main__':
    for r in gen_segments(0, 199):
        print(r)

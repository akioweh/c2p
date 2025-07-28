from sys import stdin, stdout


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


lktbl = {
    str(t): {
        str(u): (t * 10 + u) % 4 == 0
        for u in range(10)
    }
    for t in range(10)
}


s: str = input().rstrip()
s0 = '0' + s

N = len(s)
res = 0

for i, (t, u) in enumerate(zip(s0, s)):
    if lktbl[t][u]:
        res += i
    if u in '048':
        res += 1

print(f'{res}\n')

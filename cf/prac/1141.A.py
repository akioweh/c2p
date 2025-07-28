from math import log, isclose


N, M = map(int, input().split())

n = M / N
if not isclose(round(n), n):
    print(-1)
    exit()
n = int(round(n))

ans = 0
while n % 2 == 0:
    n //= 2
    ans += 1

while n % 3 == 0:
    n //= 3
    ans += 1

if n != 1:
    print(-1)
else:
    print(ans)

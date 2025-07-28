from collections import deque


N, x, y = map(int, input().split())
a = list(map(int, input().split()))


q = deque()

for i in range(len(a)):
    cur = a[i]
    while q and q[-1][0] >= cur:
        q.pop()
    q.append((cur, i))

    if q[0][1] < i - x - y:
        q.popleft()

    if i >= y and q[0][0] == a[i - y]:
        print(i - y + 1)
        exit()

# edge case for the end y elements
for i in range(len(a) - y, len(a)):
    if q[0][1] < i - x:
        q.popleft()

    if q[0][0] == a[i]:
        print(i + 1)
        exit()


N = int(input())
a = list(map(int, input().split()))

a.sort()

for i in range(N - 1):
    if a[i] != a[i + 1] and a[i + 1] < 2 * a[i]:
        print('YES')
        exit()

print('NO')

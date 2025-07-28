N = int(input())

tot = 0
for level in range(N):
    tot += (N - level - 1) * (level + 1)
    tot += 1

print(tot)

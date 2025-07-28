N = int(input())
a, b = [], []
for _ in range(N):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

a_idx = list(range(N))
a_idx.sort(key=a.__getitem__)

prev = -1
for i in a_idx:
    if b[i] < prev:
        print('Happy Alex')
        exit()
    prev = b[i]

print('Poor Alex')

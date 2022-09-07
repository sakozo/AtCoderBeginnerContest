N, X = map(int, input().split())

VP = []
for i in range(N):
    V, P = map(int, input().split())
    VP.append([V, P])

X_100 = X * 100

count = 0

for i in range(len(VP)):
    v = VP[i][0]
    p = VP[i][1]

    X_100 -= v * p
    if X_100 < 0:
        count = i + 1
        break

# print(X_100)

if count == 0:
    print(-1)
else:
    print(count)
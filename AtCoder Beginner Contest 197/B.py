H, W, X, Y = map(int, input().split())
masu = []
for _ in range(H):
    masu.append(list(input().split()))


X -= 1
Y -= 1

count = 1

for i in range(H):
    if i == 0:
        continue

    if Y - i < 0 or masu[X][Y-i] == "#":
        break

    count += 1

for i in range(H):
    if i == 0:
        continue

    if Y + i > H or masu[X][Y+i] == "#":
        break

    count += 1

for i in range(W):
    if i == 0:
        continue

    if X - i < 0 or masu[X - i][Y] == "#":
        break

    count += 1

for i in range(W):
    if i == 0:
        continue

    if X + i < 0 or masu[X + i][Y] == "#":
        break

    count += 1

print(count)

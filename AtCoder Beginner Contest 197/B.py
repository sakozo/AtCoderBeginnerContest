# https://atcoder.jp/contests/abc197/tasks/abc197_b

H, W, X, Y = map(int, input().split())
masu = []
for _ in range(H):
    masu.append(list(input()))


X -= 1 # Xが縦の座標を意味していることに注意！
Y -= 1 # Yが横の座標を意味していることに注意！

count = 1

# 上方向
for i in range(H):
    if i == 0:
        continue

    if X - i < 0 or masu[X - i][Y] == "#":
        break

    count += 1

# 下方向
for i in range(H):
    if i == 0:
        continue

    if X + i > H-1 or masu[X + i][Y] == "#":
        break

    count += 1

# 左方向
for i in range(W):
    if i == 0:
        continue

    if Y - i < 0 or masu[X][Y-i] == "#":
        break

    count += 1

# 右方向
for i in range(W):
    if i == 0:
        continue

    if Y + i > W-1 or masu[X][Y+i] == "#":
        break

    count += 1

print(count)

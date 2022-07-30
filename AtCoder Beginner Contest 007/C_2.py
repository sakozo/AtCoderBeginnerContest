# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

K = []
for _ in range(R):
    K.append(list(input()))


sy -= 1
sx -= 1
gy -= 1
gx -= 1

# メモ用二次元配列
M = []
for _ in range(R):
    M.append([-1] * C)

Q = deque()
Q.append([sy, sx])

M[sy][sx] = 0

while(len(Q) > 0):
    x, y = map(int, Q.popleft())

    for x2, y2 in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        if not (0 <= x2 < R and 0 <= y2 < C):
            continue

        if K[x2][y2] == "#":
            continue

        if M[x2][y2] == -1:
            M[x2][y2] = M[x][y] + 1
            Q.append([x2, y2])

print(M[gy][gx])


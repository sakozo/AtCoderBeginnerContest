N, S , D = map(int, input().split())
XY = []
for _ in range(N):
    XY.append(list(map(int, input().split())))

ans = "No"

for xy in XY:
    if xy[0] >= S:
        continue

    elif xy[1] <= D:
        continue

    else:
        ans = "Yes"
        break

print(ans)

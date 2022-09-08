import itertools

N = int(input())

xy_list = []

for i in range(N):
    x, y = map(int,input().split())
    xy_list.append([x, y])

ans = "No"

for xy in itertools.combinations(xy_list, 3):
    x1 = xy[0][0]
    y1 = xy[0][1]
    x2 = xy[1][0]
    y2 = xy[1][1]
    x3 = xy[2][0]
    y3 = xy[2][1]

    if (y3-y1)*(x2-x1) == (y2-y1)*(x3-x1):
        ans = "Yes"
        break

print(ans)

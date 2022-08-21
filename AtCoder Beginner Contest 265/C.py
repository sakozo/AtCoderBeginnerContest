H, W = map(int,input().split())

G = []
for _ in range(H):
    G.append(list(input()))

isContinue = True
point_i = 0
point_j = 0
roop_flg = False
log_list = []
count = 1
houmonzumi_map = []
for _ in range(H):
    houmonzumi_map.append([0] * W)

#print(houmonzumi_map)

while isContinue:
    action = G[point_i][point_j]
    log_list.append([point_i,point_j])
    if action == "U":
        if point_i == 0:
            isContinue = False
        else:
            point_i -= 1

    if action == "D":
        if point_i == H - 1:
            isContinue = False
        else:
            point_i += 1

    if action == "L":
        if point_j == 0:
            isContinue = False
        else:
            point_j -= 1

    if action == "R":
        if point_j == W - 1:
            isContinue = False
        else:
            point_j += 1

    if houmonzumi_map[point_i][point_j] >= 4:
        roop_flg = True
        # print(houmonzumi_map)
        # print(count)
        break
    else:
        houmonzumi_map[point_i][point_j] += 1
    # if len(log_list) >= 4:
    #     # point4 = log_list[count - 4]
    #     if point4[0] == point_i and point4[1] == point_j:
    #         roop_flg = True
    #         break

    count += 1

if roop_flg == True:
    print(-1)
else:
    print(point_i +1, point_j +1)
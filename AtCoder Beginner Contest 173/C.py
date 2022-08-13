H, W, K = map(int, input().split())
map = []

for i in range(H):
    map.append(list(input()))

ans = 0

for gyou_red in range(1<<H):
    for retsu_red in range(1<<W):
        black = 0

        for gyou in range(H):
            for retsu in range(W):
                if gyou_red>>gyou & 1 == 0 and retsu_red>>retsu & 1==0:
                    if map[gyou][retsu] == "#":
                        black += 1

        if black == K:
            ans += 1

print(ans)

import itertools

N, K = map(int,input().split())

T = []

for _ in range(N):
    T.append(list(map(int,input().split())))

N_list = []
for i in range(N):
    if i == 0:
        continue
    N_list.append(i)

ans = 0

candidates = itertools.permutations(N_list)

for candidate in candidates:
    time = 0
    now_place = 0
    for i in range(N-1):
        next_place = candidate[i]
        time += T[now_place][next_place]
        now_place = next_place

    time += T[now_place][0]

    if time == K:
        ans += 1

print(ans)
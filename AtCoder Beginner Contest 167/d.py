# TLE
n, k = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0
for i,_ in enumerate(range(k)):
    if i == 0:
        ans = num_list[ans]
    else:
        ans = num_list[ans-1]

print(ans)

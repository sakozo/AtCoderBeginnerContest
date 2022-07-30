S = list(input())

alp = list("abcdefghijklmnopqrstuvwxyz")

candList = []

ans = "None"

for a in alp:
    if a not in S:
        candList.append(a)

if len(candList) > 0:
    candList.sort()
    ans = candList[0]

print(ans)


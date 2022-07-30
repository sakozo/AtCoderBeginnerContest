n = int(input())
i_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i != j:
            ans += i_list[i] * i_list[j]
print(int(ans/2))

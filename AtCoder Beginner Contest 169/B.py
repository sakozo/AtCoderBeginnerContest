n = int(input())

num_list = list(map(int, input().split()))

ans = 1;
for num in num_list:
    ans *= num
    if ans > 1000000000000000000:
        ans = -1
        break

if 0 in num_list:
    ans = 0

print(ans)

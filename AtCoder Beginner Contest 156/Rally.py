n = int(input())
num_list = list(map(int, input().split()))

ans_list = [0] * (max(num_list)+1)
for i in range(max(num_list)+1):
    for j in range(n):
        ans_list[i] += ((num_list[j] - i)**2)

print(min(ans_list))

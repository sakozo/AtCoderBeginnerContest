# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

N = int(input())
p_list = list(map(int,input().split()))



#p_list2 = []
#
# ans = 0
#
# for i in range(N):
#     p_list2.append(p_list[i:N] + p_list[:i])
#
# for p2 in p_list2:
#     count = 0
#     for i in range(len(p2)):
#         if (i == (p2[i] - 1) % N) or i== p2[i] or (i == (p2[i] + 1) % N):
#             count += 1
#             if count >= N:
#                 break
#
#     ans = max(count, ans)
#
# print(ans)

ans = 0

for i in range(N):

    if i == 0:
        tmp_num1 = p_list[N-1]
        # tmp_num2 = p_list[i+1]

    if abs(p_list[i] - tmp_num1) <= N-2:
        #or abs(p_list[i] - tmp_num2) <= 2 :
        ans += 1
        if ans >= N:
            print(ans)
            exit()

    tmp_num1 = p_list[i]
    # tmp_num2 = tmp_num1

print(ans)


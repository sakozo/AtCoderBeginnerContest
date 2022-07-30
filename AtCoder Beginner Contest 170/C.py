x, n = map(int, input().split())
num_list = list(map(int, input().split()))
dif = 100000
o_list = []

if len(num_list) == 0:
    print(x)
    exit()
#
# for i in range(1, max(num_list)):
#     if i not in num_list:
#         o_list.append(i)

for i in range(-1000, 1000):
    if i not in num_list:
        o_list.append(i)

o_list.sort(reverse=True)

for num in o_list:
    if abs(x - num) <= dif:
        # if x not in num_list:
        dif = abs(x -num)
        ans = num

print(ans)

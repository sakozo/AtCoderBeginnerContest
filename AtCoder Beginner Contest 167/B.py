# a, b, c, k = map(int, input().split())
# list1 = [1] * a
# list0 = [0] * b
# list_m1 = [-1] * c
#
# list1.extend(list0)
# list1.extend(list_m1)
#
# list1.sort(reverse=True)
#
# ans = 0
# for i in range(k):
#     ans += list1[i]
#
# print(ans)

a, b, c, k = map(int, input().split())
ans = 0
if k <= a:
    ans = k
elif k <= a+b:
    ans = a
else:
    ans = a + (-1)*(k-a-b)
print(ans)

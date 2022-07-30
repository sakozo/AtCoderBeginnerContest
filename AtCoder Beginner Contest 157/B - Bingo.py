def my_index(l, x, default=-1):
    if x in l:
        return l.index(x)
    else:
        return default


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list(map(int, input().split()))
N = int(input())
num_list = [int(input()) for _ in range(N)]

list1.extend(list2)
list1.extend(list3)
hit_list = [0] * 9

for num in num_list:
    res = my_index(list1, num)
    if res != -1:
        hit_list[res] += 1

if (hit_list[0] > 0 and hit_list[1] > 0 and hit_list[2] > 0) or (
        hit_list[3] > 0 and hit_list[4] > 0 and hit_list[5] > 0) or (
        hit_list[6] > 0 and hit_list[7] > 0 and hit_list[8] > 0):
    print('Yes')
elif (hit_list[0] > 0 and hit_list[3] > 0 and hit_list[6] > 0) or (
        hit_list[1] > 0 and hit_list[4] > 0 and hit_list[7] > 0) or (
        hit_list[2] > 0 and hit_list[5] > 0 and hit_list[8] > 0):
    print('Yes')
elif (hit_list[0] > 0 and hit_list[4] > 0 and hit_list[8] > 0) or (
        hit_list[2] > 0 and hit_list[4] > 0 and hit_list[6] > 0):
    print('Yes')
else:
    print('No')

N = int(input())

if N == 1:
    print(1)
    exit()

count_dic = {}
for i in range(N+1):
    i_tmp = i
    count = 0
    while True:
        if i == 0:
            break
        elif i_tmp % 2 == 0:
            i_tmp = i_tmp / 2
            count += 1
        else:
            break
    count_dic[i] = count
print(max(count_dic, key=count_dic.get))

###########################################
list = [64,32,16,8,4,2]
O = int(input())
if O == 1:
    print(1)
    exit()

for num in list:
    if O >= num:
        print(num)
        break

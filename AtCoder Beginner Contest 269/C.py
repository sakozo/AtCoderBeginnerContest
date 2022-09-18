# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

X = int(input())

# bin_num = format(X,'b')
# print(bin_num)
# print(int(bin_num,2))

bin_num = format(X,'b')

bin_num_list = []
# print(bin_num)
# for i in range(len(bin_num)):

# X = int(input())
# bin_num = format(X,'b')
# n = len(bin_num)

keta_list = []
for i in range(len(bin_num)):
    if str(bin_num)[i] == '1':
        keta_list.append(i)
n = len(keta_list)
# print(keta_list)

# for keta in keta_list:
#     len(bin_num) - keta
comb_list = []
for bit in range(1 << n):
    combination = []
    for i in range(n):
        shift_i = 1 << i
        if bit & shift_i > 0:
            combination.append(keta_list[i])
    comb_list.append(combination)

for c in comb_list:
    if len(c) == 0:
        continue
    tmp_num=0
    for num in c:
        tmp_num += 10 ** (len(bin_num) - num -1)
    bin_num_list.append(tmp_num)
# print(bin_num_list)
num_list = [0]
for bin_num in bin_num_list:
    num_list.append((int(str(bin_num),2)))
# print(num_list)
num_list.sort()
for num in num_list:
    print(num)
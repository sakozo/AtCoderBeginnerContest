input = int(input())
list = []

for i in range(1,10):
    for j in range(1,10):
        list.append(i*j)

if input in list:
    print("Yes")
else:
    print("No")

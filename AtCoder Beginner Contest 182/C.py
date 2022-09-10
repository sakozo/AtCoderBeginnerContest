N = int(input())

count_remainder_1 = 0

count_remainder_2 = 0

full_remainder = N % 3

N = str(N)

for i in range(len(N)):
    num = N[i]

    if int(num) % 3 == 1:
        count_remainder_1 += 1
    elif int(num) % 3 == 2:
        count_remainder_2 += 1

if full_remainder == 0:
    print(0)
    exit()

if full_remainder == 1:
    if count_remainder_1 > 0:
        if len(N) > 1:
            print(1)
            exit()
        else:
            print(-1)
            exit()
    elif count_remainder_2 > 1:
        if len(N) > 1:
            print(2)
            exit()
        else:
            print(-1)
            exit()
    else:
        print(-1)
        exit()

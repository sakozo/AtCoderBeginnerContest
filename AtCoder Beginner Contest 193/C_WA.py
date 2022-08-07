N = int(input())

count = 0

for a in range(2, 10**5 + 10):
    for b in range(2, 50):
        if a ** b <= N:
            count += 1
        else:
            break

print(N - count)

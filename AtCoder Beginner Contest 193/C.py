N = int(input())

# 重複を許さないsetを定義
num_set = set()

for a in range(2, 10 ** 5 +1):
    for b in range(2, 35):
        num = a ** b
        if num <= N:
            num_set.add(num)
        else:
            break

print(N - len(num_set))

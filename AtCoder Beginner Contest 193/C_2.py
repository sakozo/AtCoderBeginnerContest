N = int(input())

num_set = set()

for a in range(2, 10**5):
    for b in range(2, 33):
        result = a ** b
        if result <= N:
            num_set.add(result)
        else:
            break

print(N - len(num_set))
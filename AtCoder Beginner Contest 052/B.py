N = int(input())
S = list(input())

max_count = 0
count = 0

for s in S:
    if s == "I":
        count += 1
        max_count = max(count,max_count)
    else:
        count -= 1

print(max_count)

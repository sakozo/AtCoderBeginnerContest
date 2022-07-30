N, X = map(int, input().split())
A = list(map(int, input().split()))

ans_list = []

for a in A:
    if a == X:
        continue
    else:
        ans_list.append(str(a))

print(" ".join(ans_list))


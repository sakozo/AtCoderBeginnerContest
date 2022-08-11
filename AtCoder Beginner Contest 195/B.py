A, B , W = map(int, input().split())

WG = W * 1000

ans_min = 10 ** 10
ans_max = -1

for x in range(1, 10 ** 6 + 1):
    if A * x <= WG <= B * x:
        ans_min = min(x, ans_min)
        ans_max = max(x, ans_max)

if ans_min == 10 ** 10:
    print("UNSATISFIABLE")
else:
    print(ans_min,ans_max)

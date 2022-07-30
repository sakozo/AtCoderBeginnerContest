A, B, C = map(int, input().split())

ans = ""

if A**2 + B ** 2 < C**2:
    ans = "Yes"
else:
    ans = "No"

print(ans)

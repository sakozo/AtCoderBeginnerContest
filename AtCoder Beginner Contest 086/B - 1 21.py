a, b = map(str, input().split())

num = int(a+b)

ans = "No"
i = 0
while i*i <= num:
    if i*i == num:
        ans = "Yes"
    i += 1

print(ans)

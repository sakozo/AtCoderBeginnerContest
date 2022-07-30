A, B = map(int, input().split())
S = input()

s_list = S.split('-')

ans = "Yes"

if len(s_list) != 2:
    ans = "No"
else:
    if "-" in s_list[0] or len(s_list[0]) != A or "-" in s_list[1] or len(s_list[1]) != B:
        ans = "No"

print(ans)


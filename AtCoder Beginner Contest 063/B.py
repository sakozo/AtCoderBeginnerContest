S = input()
s_list = list(S)

chek_list = []
ans = "yes"
for s in s_list:
    if s in chek_list:
        ans = "no"
        break
    else:
        chek_list.append(s)

print(ans)

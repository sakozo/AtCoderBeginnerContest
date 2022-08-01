N = int(input())

def judge_ten(n):
    n_str = str(n)
    if '7' in n_str:
        return True
    else:
        return False

def judge_eight(x):
    s = ""
    while x > 0:
        s = str(x%8) + s
        x //= 8
    if "7" in s:
        return True
    else:
        return False


count = 0

for i in range(1, N+1):
    if not judge_ten(i) and not judge_eight(i):
        count += 1

ans = count
print(ans)
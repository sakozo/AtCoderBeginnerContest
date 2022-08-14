H1, W1 = map(int, input().split())
A = []

for i in range(H1):
    A.append(list(input().split()))

H2, W2 = map(int, input().split())
B = []

for i in range(H2):
    B.append(list(input().split()))


memo = []
for i in range(H1):
    memo.append([False] * W1)


for i in range(H2):
    for j in range(W2):
        for k in range(H1):
            for l in range(W1):
                if B[i][j] == A[k][l]:
                    memo[k][l] = True

check_list = []
ans = "Yes"

for i in range(H1):
    if True in memo[i] and len(check_list) == 0:
        check_list = memo[i]
    if True in memo[i]:
        for j in range(W1):
            if not check_list[j] == memo[i][j]:
                ans = "No"
                break

if len(check_list) == 0:
    ans = "No"

print(ans)


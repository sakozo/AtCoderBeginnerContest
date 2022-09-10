# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

S = list(input())
T = list(input())

ans = "Yes"

if len(S) > len(T):
    ans = "No"
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            ans = "No"

print(ans)

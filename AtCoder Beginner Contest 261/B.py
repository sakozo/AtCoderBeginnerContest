# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))
N = int(input())

hyo = []
for _ in range(N):
    A = list(input())
    hyo.append(A)

ans = "correct" # incorrect

for i in range(N):
    for j in range(N):
        A = hyo[i][j]
        B = hyo[j][i]

        if A == "W":
            if B != "L":
                ans = "incorrect"
                break
        if A == "L":
            if B != "W":
                ans = "incorrect"
                break
        if A == "D":
            if B != "D":
                ans = "incorrect"
                break

print(ans)

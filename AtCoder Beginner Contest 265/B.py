N, M, T = map(int,input().split())
A = list(map(int,input().split()))
XY = []
for _ in range(M):
    XY.append(list(map(int,input().split())))

bonus_list = [0] * (N -1)
for xy in XY:
    bonus_list[xy[0]-2] = xy[1]
# print(A)
# print(bonus_list)

ans = "Yes"

for i in range(N-1):
    T -= A[i]

    if T <= 0:
        ans = "No"
        break

    T += bonus_list[i]

print(ans)
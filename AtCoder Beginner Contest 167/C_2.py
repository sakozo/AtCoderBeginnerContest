N, M, X = map(int, input().split())

C = []
A = []

for i in range(N):
    CA = list(map(int,input().split()))
    C.append(CA[0])
    A.append(CA[1:])

ans = 10 ** 10

for i in range(2 ** N):
    cost = 0
    skill = [0] * M

    for shift in range(N):
        if i >> shift & 1 == 1:
            cost += C[shift]
            for j in range(M):
                skill[j] += A[shift][j]

    if X <= min(skill):
        ans = min(ans, cost)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)

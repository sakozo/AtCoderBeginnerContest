N, P, Q, R = map(int,input().split())
A = list(map(int,input().split()))
A_ruiseki = []
pre_ruiseki = 0
for i in range(N):
    A_ruiseki.append(A[i] + pre_ruiseki)
    pre_ruiseki = A[i] + pre_ruiseki


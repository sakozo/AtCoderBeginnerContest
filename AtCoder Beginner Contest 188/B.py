N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

t = 0

for i in range(N):
    t += A[i] * B[i]

if t == 0:
    print("Yes")
else:
    print("No")

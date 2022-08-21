# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

X, Y, N = map(int,input().split())

ans = 0

if X >= Y/3:
    ans += (N // 3) * Y
    ans += N % 3 * X
else:
    ans += N * X

print(ans)

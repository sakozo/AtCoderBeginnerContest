N, A, B = map(int,input().split())

ans = 0

if N <= A:
    ans = N
else:
    c = N // (A + B)
    d = N % (A + B)

    ans = A * c
    if d <= A:
        ans += d
    else:
        ans += A

print(ans)

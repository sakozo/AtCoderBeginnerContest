# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

L1, R1, L2, R2 = map(int,input().split())

ans = 0

start = 0
end = 0

if L1 >= L2:
    start = L1
else:
    start = L2

if R1 >= R2:
    end = R2
else:
    end = R1

if end - start <= 0:
    ans = 0
else:
    ans = end - start

print(ans)
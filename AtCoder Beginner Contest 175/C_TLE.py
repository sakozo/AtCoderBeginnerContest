X, K, D = map(int,input().split())

position = X

for i in range(K):
    light = position + D
    left = position - D

    if abs(0 - light) <= abs(0 - left):
        position = light
    else:
        position = left

ans = abs(0 - position)

print(ans)
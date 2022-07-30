# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))
import itertools

N, M = map(int,input().split())
X = list(map(int,input().split()))

C = {}
for _ in range(M):
    #C.append(list(map(int,input().split())))
    A, B = map(int, input().split())
    C[A] = B

pattern = []

nums = [True, False]
for balls in itertools.product(nums, repeat=N):
    if balls.count(False) > N // 2:
        continue
    pattern.append(balls)

max_score = 0

for pat in pattern:
    i = 0
    score = 0
    count = 0
    for p in pat:

        if p:
            score += X[i]
            count += 1
        else:
            count = 0

        if count in C:
            score += C[count]

        max_score = max(max_score, score)
        i += 1


print(max_score)





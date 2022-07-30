N = int(input())
mountains = []

for _ in range(N):
    N, H = input().split()
    mountains.append([int(H), N])

mountains.sort(reverse=True)

print(mountains[1][1])
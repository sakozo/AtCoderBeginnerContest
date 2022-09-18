# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))
MAP = [list(input()) for _ in range(10)]

i1 = -1
i2 = -1
j1 = -1
j2 = -1

for i in range(10):
    for j in range(10):
        if MAP[i][j] == '#':
            if i1 == -1:
                i1 = i
            i2 = i

M = MAP[i1]
for k in range(10):
    if M[k] == '#':
        if j1 == -1:
            j1 = k
        j2 = k

# print(i1)
# print(i2)
# print(j1)
# print(j2)

print(i1 + 1, i2 +1)
print(j1 + 1, j2 +1)

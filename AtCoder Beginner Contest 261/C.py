# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

N = int(input())
S = []
for _ in range(N):
    S.append(input())

# print(S)

S_work = S.copy()

s_map = dict()

for s in S:
    if s in s_map:
        print(s + "(" + str(s_map[s]) + ")")
        num = s_map[s] + 1
        s_map[s] = num
    else:
        s_map[s] = 1
        print(s)
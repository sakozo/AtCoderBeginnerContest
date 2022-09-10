# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))

# A, B, C, D, E = map(int,input().split())
# list = []

n_list = list(map(int,input().split()))
ans = []
for n in n_list:
    if n not in ans:
        ans.append(n)

print(len(ans))
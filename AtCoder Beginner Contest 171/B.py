from numpy import sort

a,b = map(int,input().split())
num_list = list(map(int,input().split()))

num_list.sort()

ans = sum(num_list[:b])

print(ans)

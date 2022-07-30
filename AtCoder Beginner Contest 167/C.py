import numpy as np
import itertools

n, m, x = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]

ans = -1

num_list.sort(key=lambda x: x[0])

result = []
for n1 in range(1,len(num_list)+1):
    for conb in itertools.combinations(num_list, n1):
        result.append(np.sum(conb, axis=0))

result.sort(key=lambda x: x[0])

for r in result:
    if min(r[1:]) >= x:
        ans = r[0]
        break

print(ans)

# お手上げ
from operator import itemgetter

N, M = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(N)]
#num_list.sort(reverse=True)
for l in num_list:
    l.sort(reverse=True)
num_list.sort(reverse=True)
#a = sorted(num_list, key=itemgetter(1))
print(num_list)


room_list = []
for i in range(N):
    room_list.append(i)

print(room_list)

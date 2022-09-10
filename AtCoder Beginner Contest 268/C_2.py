N = int(input())
p_list = list(map(int, input().split()))

count = [0] * N

for i in range(N):
    for j in range(3):
        print('i : {}'.format(i))
        print('j : {}'.format(j))
        a = (p_list[i] - 1 - i + j + N) % N
        print('(p_list[i] - 1 - i + j + N) % N : {}'.format(a))
        count[(p_list[i] - 1 - i + j + N) % N] += 1

print(count)

ans = 0

for i in range(N):
    ans = max(ans, count[i])

print(ans)
N = int(input())
h = list(map(int, input().split()))

# cost[i]:足場iにたどり着くための最小コスト。サイズNを確保する
cost = [0] * N

# 初期条件
cost[0] = 0
# 2つ目の足場はジャンプ元が１通り
cost[1] = cost[0] + abs(h[0] - h[1])
# それ以降の足場はジャンプ元が２通りあるため、コストが小さいほうを採用する
for i in range(2, N):
    cost[i] = min(cost[i-1] + abs(h[i-1] - h[i]), cost[i-2] + abs(h[i-2] - h[i]))

# 答えは最後の愛馬までの最小コスト
print(cost[N-1])

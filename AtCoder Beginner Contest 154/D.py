N, K = map(int,input().split())
p = list(map(int,input().split()))

# 期待値を格納する配列を定義
p_ex = []

for i in range(N):
    # 期待値は(1 + 面数) / 2で算出
    p_ex.append((1 + p[i]) / 2)

# 累積和を格納しておく配列
p_ex_ruiseki = []
pre_ruiseki = 0
for i in range(N):
    p_ex_ruiseki.append(pre_ruiseki + p_ex[i])
    pre_ruiseki = pre_ruiseki + p_ex[i]

max_ans = -1

# 最大値を探索
for x in range(N - K + 1):
    if x == 0:
        max_ans = max(p_ex_ruiseki[x + K -1], max_ans)
    else:
        max_ans = max(p_ex_ruiseki[x + K -1] - p_ex_ruiseki[x -1], max_ans)

print(max_ans)


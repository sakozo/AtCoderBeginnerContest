# WAあり AC×20 WA×11

from math import ceil

# X:開始地点
# K:移動回数
# D:移動距離
X, K, D = map(int, input().split())

ans = -1

if abs(X) - (K * D) > 0:
    # 一方向に移動し続けても0に到達しない
    ans = abs(0 - (abs(X) - (K * D)))
elif abs(X) - (K * D) == 0:
    # 一方向に移動し続けてちょうど0の上で終了
    ans = 0
else:
    # 0を一度飛び越える
    over_count = ceil(abs(X) / D)
    if (K - over_count)%2 == 0:
        # 残りの移動回数が偶数の場合
        last_dist = abs(X) - (K * over_count)
        ans = abs(0 - last_dist)
    else:
        # 残りの移動回数が奇数の場合
        last_dist = abs(X) - (K * (over_count-1))
        ans = abs(0 - last_dist)

print(ans)
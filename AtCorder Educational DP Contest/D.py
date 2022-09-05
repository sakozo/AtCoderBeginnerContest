# 入力受け取り
N, W = map(int, input().split())
# 1インデックスにするために 0,0を埋めておく
items = [[0, 0]]
# 入力受け取り
for i in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

# 二次元配列（表）の形で考える
dp = [[0] * (W + 1) for i in range(N+1)]

# １行ずつループ
for gyou_i in range(1, N+1):
    # １列ずつループ
    for retsu_w in range(W+1):
        # 行+列のループで左上から表を埋めていく

        # 入力で受け取った商品の重さと価値を取り出す
        w,v = items[gyou_i]

        if retsu_w - w < 0:
            # 重さが大きくて、ナップザックに入らない場合
            dp[gyou_i][retsu_w] = dp[gyou_i - 1][retsu_w]
        else:
            # 商品を入れるor入れないを選択できる状態

            # 商品を入れない選択をした場合の価値
            red = dp[gyou_i - 1][retsu_w]
            # 商品を入れる選択をした場合の価値
            blue = dp[gyou_i - 1][retsu_w - w] + v

            # 商品を入れるor入れない　大きい方を採用する
            dp[gyou_i][retsu_w] = max(red, blue)

# 表の最後（右下）を解答として出力する
print(dp[N][W])

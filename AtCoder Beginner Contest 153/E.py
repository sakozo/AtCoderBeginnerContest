# H:モンスターの体力
# N:使える魔法の種類
H, N = map(int, input().split())

# 大きい値で初期化
dp = [10 ** 10] * (H + 1)

# 分かるところはすぐに埋める
dp[0] = 0

for i in range(N):
    # 入力の受け取り回数ループする
    A, B = map(int, input().split())

    for h in range(H + 1):
        # モンスターの体力分ループする

        # h:今までにモンスターに与えた攻撃の累計
        # A:今から与える攻撃力
        if h + A <= H:
            # モンスターの体力内で収まる場合

            dp[h+A] = min(dp[h+A], dp[h] + B)
        else:
            # モンスターの体力を超える場合

            dp[H] = min(dp[H], dp[h] + B)
    # デバッグ用出力
    # print(dp)

print(dp[H])

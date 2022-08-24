# 二分探索

# 値を計算するメソッド
def price(N):
    N_str = str(N)
    d=len(N_str)
    return A*N + B*d

A, B, X = map(int, input().split())

# 1も買えない場合
if X < price(1):
    print(0)
    exit()

######################################
# 左端の値をセット（最小値）
left = 1
# 右端の値をセット（最大値）
right = 10 ** 20

# whileの終了条件は、(右端-左端) の差が1より小さい　両側から切り詰めていってピッタリ一つに決まる
while 1 < right - left:
    # 中央の値を計算
    N = (left + right) // 2

    if price(N) <= X:
        # 目標値より低い場合、最小値を押し上げてよいのでleftを大きい値で更新
        left =N
    else:
        # 目標値より大きい場合、最大値を押し下げてよいのでrightを小さい値で更新
        right = N

######################################

# Maxでも買える場合
if 10 ** 9 < left:
    left = 10** 9

# 答えになるのは二分探索してピッタリ一つに決まった値
print(left)
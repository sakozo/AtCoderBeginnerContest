import itertools

N, K = map(int, input().split())

time = []

for i in range(N):
    T = list(map(int, input().split()))
    time.append(T)

ans = 0



for root in itertools.permutations(range(1,N)):
    # 経過時間を格納する変数の初期化
    now_time = 0
    # 都市１からスタートして次の都市に移動する時間を加算
    now_time += time[0][root[0]] # time[0]:都市1 root[0]:次に移動するのにかかる時間
    # 移動先の都市を格納
    now_city = root[0]

    for i in range(1, N-1):  # 2番目の都市から1回ずつ訪問を全パターン調べる
        to_city = root[i]  # 移動後の都市を取得
        now_time += time[now_city][to_city]  # 現在地点から次の都市へ行くためにかかる時間を加算
        now_city = to_city  # 現在地点を更新

    now_time += time[now_city][0]  # 都市1に戻ってくる時間を加算

    if now_time == K:  # 移動時間の合計がちょうどKになる場合
        ans += 1

print(ans)
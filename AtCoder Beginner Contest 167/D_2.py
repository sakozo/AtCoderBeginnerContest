# 周期性がある問題

N, K = map(int, input().split())
# 1インデックスにするためにリストの先頭を埋めておく
A = [0] + list(map(int,input().split()))

# 訪問したことを記録するリストを定義
visited = [-1] * (N+1)
visited[1] = 0  # 1インデックスにするためにリストの先頭を埋めておく

# 現在地
now_town = 1
# 移動回数
move_cnt = 0

for i in range(10**6):
    move_cnt += 1  # 移動回数カウントアップ
    now_town = A[now_town]  # Aのリストから現在地のインデックスを取得すると次の地点が得られる

    if move_cnt == K:  # 移動回数が規定の回数に達した場合終了
        print(now_town)
        exit()

    if visited[now_town] == -1:
        # 初めて訪問する地点の場合
        visited[now_town] = move_cnt  # 記録用リストに何回目の移動で到達したかメモをする
    else:
        # 二回目に訪問する地点の場合
        # ループし始めることが分かるのでループする移動回数を計算する
        cycle = move_cnt - visited[now_town]  # 今の移動回数 - 今いる地点を前回訪問した時の移動回数 = ループするまでの移動回数
        break

# for文の中で移動した回数を引く
K -= move_cnt
# 周期性がある中でループし続けた最後の余りが分かればよいので余りをとる
K %= cycle
# 残りの移動回数から最終地点をたどる
for i in range(K):
    now_town = A[now_town]

print(now_town)

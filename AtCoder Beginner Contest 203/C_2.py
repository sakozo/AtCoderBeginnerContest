# N: 友達の数　K: 最初に持っているお金
N, K = map(int, input().split())

# A: 友達がいる村 B:もらえるお金
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append([A,B])

# 友達がいる村の昇順でソート
AB.sort()

# お金を保持する変数　初期値はK
# ここで管理するお金は今までもらったお金の合計、街を移動するたびに引かない
money = K

# 友達の数だけループすることで時間内に完了できる　(1≤N≤2×10^5)
for i in range(N):
    # 友達がいる村
    now_village = AB[i][0]
    # もらえるお金
    get_money = AB[i][1]

    if money - now_village < 0:
        # 次の友達がいる村にたどり着けない場合
        # 今までもらったお金の合計が最終到達点 答えを出力してexit
        stop_village = money
        print(stop_village)
        exit()
    else:
        # 次の友達がいる街にたどり着ける場合
        # お金を加算する
        money += get_money

print(money)

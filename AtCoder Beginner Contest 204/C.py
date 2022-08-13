from collections import deque

N, M = map(int, input().split())

# 空の二次元配列を用意する
road_list = [[] for i in range(N+1)]

# 各都市から行ける都市を二次元配列に格納
# road_list[1] で取得する配列は都市1から行くことができる都市のリスト
for _ in range(M):
    A, B = map(int,input().split())
    road_list[A].append(B)

Q = deque()
count = 0

# スタート地点は各都市１回ずつ
for i in range(1, N+1):
    # 訪問済みメモを用意する
    visited = [False] * (N+1)
    visited[i] = True
    count += 1

    # キューにスタート地点を格納
    Q.append(i)

    # キューの中がある内はループを続ける
    while len(Q) > 0:
        # 現在地を取り出す
        now_city = Q.popleft()
        # 現在地から次に行ける都市を１つずつ調べる
        for next_city in road_list[now_city]:
            if visited[next_city] == False:
                # 未訪問だった場合、訪問済みにする
                visited[next_city] = True
                count += 1
                # 次の現在地にする
                Q.append(next_city)

print(count)

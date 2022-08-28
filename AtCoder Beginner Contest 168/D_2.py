N, M = map(int, input().split())

# 空の二次元配列を作成、1インデックスにするために、0は使わない
connect = [ [] for i in range(N+1) ]

# 二次元配列
# connect[i] で取得できる配列 = 部屋iから行ける部屋
for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

# 訪問済みを格納するリスト
visited = [False] * (N+1)
# 1の部屋は最初に訪問済みにする
visited[1] = True

from collections import deque
que = deque()
que.append(1)

#  道しるべを格納するリスト
ans = [0] * (N+1)

# 幅優先探索
while 0 < len(que):
    # 今の部屋
    now_room = que.popleft()
    # 今の部屋から行ける部屋を１つずつ取り出して確認
    for to_room in connect[now_room]:
        # 候補の部屋が未訪問だった場合
        if visited[to_room] == False:
            # 部屋を訪問済みにする
            visited[to_room] = True
            # 今の部屋を道しるべとして追加する
            ans[to_room] = now_room
            # キューに次の部屋を格納する
            que.append(to_room)

print("Yes")

for i in range(2,N+1):
    print(ans[i])

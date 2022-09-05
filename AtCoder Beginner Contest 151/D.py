# 入力受け取り
H, W = map(int,input().split())

# 迷路を二次元配列で扱う
maze = []

# 入力受け取り
for i in range(H):
    # 文字列を配列で受け取る
    maze.append(list(input()))

from collections import deque

def count_steps(start_gyou, start_retsu):
    """
    スタートからゴールまでの最大歩数をカウントする
    :param start_gyou:int
    　スタート地点のY座標
    :param start_retsu:int
    　スタート地点のX座標
    :return:int
    　最大歩数
    """

    # 歩数を記録する表を定義　初期値は未訪問を意味する -1
    maze_count = [[-1] * W for i in range(H)]
    # スタート地点は 0をセット
    maze_count[start_gyou][start_retsu] = 0

    # 幅優先探索で使うキューを準備する
    que = deque()
    que.append([start_gyou, start_retsu])

    # ループの継続条件はキューが空になるまで
    while len(que) > 0:
        # キューから取り出す
        # 今のY座標とX座標
        now_gyou, now_retsu = que.popleft()
        # 今の位置に来る歩数
        now_count = maze_count[now_gyou][now_retsu]

        # 左
        if 0 <= now_gyou - 1 < H and 0 <= now_retsu < W:
            # 左に進んでも外枠外に出ない
            if maze[now_gyou - 1][now_retsu] == ".":
                # 左に進んでも通路である（壁でない）
                if maze_count[now_gyou - 1][now_retsu] == -1:
                    # 左に進んでも未訪問である

                    # 左のマスを歩数を +1 にしてキューに加える
                    maze_count[now_gyou - 1][now_retsu] = now_count + 1
                    que.append([now_gyou - 1, now_retsu])
        
        # 右
        if 0 <= now_gyou + 1 < H and 0 <= now_retsu < W:
            if maze[now_gyou + 1][now_retsu] == ".":
                if maze_count[now_gyou + 1][now_retsu] == -1:
                    maze_count[now_gyou + 1][now_retsu] = now_count + 1
                    que.append([now_gyou + 1, now_retsu])

        # 上
        if 0 <= now_gyou < H and 0 <= now_retsu - 1 < W:
            if maze[now_gyou][now_retsu - 1] == ".":
                if maze_count[now_gyou][now_retsu - 1] == -1:
                    maze_count[now_gyou][now_retsu - 1] = now_count + 1
                    que.append([now_gyou, now_retsu - 1])

        # 下
        if 0 <= now_gyou < H and 0 <= now_retsu + 1 < W:
            if maze[now_gyou][now_retsu + 1] == ".":
                if maze_count[now_gyou][now_retsu + 1] == -1:
                    maze_count[now_gyou][now_retsu + 1] = now_count + 1
                    que.append([now_gyou, now_retsu + 1])

    # 返却用の変数を定義
    max_count = 0
    # 歩数の最大値を取り出す
    for gyou in range(H):
        for retsu in range(W):
            max_count = max(max_count, maze_count[gyou][retsu])

    return max_count

ans = 0

for gyou in range(H):
    for retsu in range(W):
        if maze[gyou][retsu] == ".":
            # 壁でない位置をすべてスタート地点としてメソッド呼び出しを行い、最大値を保持し続ける
            ans = max(ans, count_steps(gyou,retsu))

print(ans)
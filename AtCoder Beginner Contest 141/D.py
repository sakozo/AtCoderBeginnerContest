# N:商品の数　M:割引券の数
N, M = map(int, input().split())
# 商品の値段のリスト
A = list(map(int, input().split()))

# ヒープを利用する前準備
#  ヒープでは最小値を取り出すため
#  最大値を取り出したい場合は、-1をかけておく
A_minus = []
for i in range(N):
    A_minus.append(-1 * A[i])

# ヒープをインポート
import heapq

# リストをヒープ化する
heapq.heapify(A_minus)

# 商品券の数だけループする
for i in range(M):
    # 最小値を取り出す
    X = heapq.heappop(A_minus)
    # 取り出した値を2でわる
    X /= 2
    # 小数点以下を丸める
    X = int(X)
    # ヒープに戻す
    heapq.heappush(A_minus, X)

# 合計を計算し、正の値に戻したものが解答
ans = -1 * sum(A_minus)
print(ans)
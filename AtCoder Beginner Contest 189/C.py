N = int(input())
A = list(map(int, input().split()))

ans = -1

# l:範囲の左端
for l in range(N):
    # l~rの範囲内の皿に乗っているオレンジの個数の最小値を格納する
    A_min = A[l]
    # r:範囲の右端
    for r in range(l, N):
        # 右端の範囲を広げたらオレンジの個数の最小値を更新する
        A_min = min(A_min, A[r])
        # 左右の範囲が決まったら結果値を計算して、過去最大なら更新する
        ans = max(ans, A_min * (r - l + 1))

print(ans)

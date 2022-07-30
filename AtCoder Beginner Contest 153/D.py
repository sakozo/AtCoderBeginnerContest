# TODO:20220718×

H = int(input())

ans = 0
count = 1

while H > 0:
    ans += count
    H //= 2
    count *= 2

print(ans)

# 4
# 2 2
# 1 1 1 1
# 1 1 1 1
# H とどめをさすのに必要な手数
# 1 初めは1体
# 2 2回目は2体
# 2の0乗 2の1乗って増えていって1になったらH回攻撃して終了

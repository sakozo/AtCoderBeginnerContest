K, N = map(int, input().split())
house_list = list(map(int, input().split()))

dif_list = []  # 家の間の距離を格納する配列
for i, l in enumerate(house_list):
    if i == 0:  # 0番目はスキップ
        continue
    dif_list.append(house_list[i] - house_list[i - 1])  # 配列に押し込む

dif_last_start = K - house_list[-1] + house_list[0]  # 最後の家と最初の家の距離

if dif_last_start < max(dif_list):  # dif_list配列ないの最大の距離よりも最後と最初を跨いだ方が近いなら
    ans = sum(dif_list) - max(dif_list) + dif_last_start
else:
    ans = sum(dif_list)

print(ans)

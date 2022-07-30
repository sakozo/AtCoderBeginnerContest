def main():
    N = int(input())
    q_list = list(map(int, input().split()))
    num = len(q_list)

    q_list.sort()  # 昇順並べ替え

    ans = q_list[int(num / 2)] - q_list[int(num / 2 - 1)]  # 半分の分かれ目の数字のさを取る
    print(ans)


if __name__ == '__main__':
    main()

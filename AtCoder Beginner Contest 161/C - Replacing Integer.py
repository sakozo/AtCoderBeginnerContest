def main():
    N, K = map(int, input().split())

    remainder = N % K
    if abs(remainder - K) < remainder:
        ans = abs(remainder - K)
    else:
        ans = remainder
    print(ans)


if __name__ == '__main__':
    main()

# TLE ####################################
# def main():
#     N, K = map(int, input().split())
#
#     min_num = N
#     while True:
#         dif = abs(min_num - K)
#         if dif < min_num:
#             min_num = dif
#         else:
#             break
#     print(min_num)
# if __name__ == '__main__':
#     main()

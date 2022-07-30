def main():
    N, M = map(int, input().split())

    all = (N + M) * (N + M - 1) / 2
    odd = N * M
    ans = int(all - odd)
    print(ans)


if __name__ == '__main__':
    main()

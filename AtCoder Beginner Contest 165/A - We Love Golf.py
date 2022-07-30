def main():
    K = int(input())
    A, B = map(int, input().split())

    if A % K == 0 or B % K == 0:
        ans = "OK"
    elif A//K != B//K:
        ans = "OK"
    else:
        ans = "NG"

    print(ans)


if __name__ == '__main__':
    main()

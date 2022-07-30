def even(num):
    return int(num / 2)


def odd(num):
    return 3 * num + 1


def main():
    s = int(input())
    tmp = s
    list = [s] * 1
    i = 0

    while True:
        i += 1
        if tmp % 2 == 0:
            tmp = even(tmp)
        else:
            tmp = odd(tmp)
        if tmp in list:
            break
        list.append(tmp)

    ans = i + 1
    print(ans)


if __name__ == '__main__':
    main()

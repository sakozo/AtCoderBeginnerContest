def main():
    s = list(input())
    count_list = [0] * 1
    index = 0
    for i in s:
        if i == "A" or i == "T" or i == "G" or i == "C":
            count_list[index] += 1
        else:
            index += 1
            count_list.append(0)

    ans = max(count_list)

    print(ans)


if __name__ == '__main__':
    main()

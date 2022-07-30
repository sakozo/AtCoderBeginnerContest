import math


def is_prme_number(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def main():
    x = int(input())
    while True:
        if is_prme_number(x):
            break
        x += 1
    print(x)


if __name__ == '__main__':
    main()

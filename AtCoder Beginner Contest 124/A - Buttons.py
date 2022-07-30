a, b = map(int, input().split())

if a == b:
    ans = a + b
else:
    ans = max(a, b) + max(a-1, b -1)

print(ans)


# def main():
#     num_list = list(map(int, input().split()))
#
#     sorted(num_list, reverse=True)
#
#     if num_list[0] -1 >= num_list[1]:
#         ans = num_list[0] + num_list[0] -1
#     else:
#         ans = num_list[0] + num_list[1]
#
#     print(ans)
#
#
# if __name__ == '__main__':
#     main()

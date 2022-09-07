def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def make_divisors(n):
    divisor_list = []
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            divisor_list.append(i)
            if i != N//i:
                divisor_list.append(i)
    divisor_list.sort()
    return divisor_list

N = int(input())
list_ans = make_divisors(N)
for ans in list_ans:
    print(ans)

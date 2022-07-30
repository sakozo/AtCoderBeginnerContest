##未完成
import sympy
import numpy as np

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(int(i))
    i += 1
  if n > 1:
    table.append(int(n))
  return table

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

def all_the_same(elements):
    return elements[1:] == elements[:-1]

def main():
    n = int(input())

    ans = 0
    num_list = []

    div_list = sympy.divisors(n)

    while n > 1:
        for d in div_list:
            res = prime_decomposition(d)
            if len(res) > 0:
                res.sort()
                if d not in num_list:
                    if not all_the_same(res):
                        continue
                    num_list.append(d)
                    n = n/d
                    ans += 1
                    if n < 1:
                        break

    print(ans)


if __name__ == '__main__':
    main()

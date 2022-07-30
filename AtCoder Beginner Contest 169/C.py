from decimal import *
import math

a, b = input().split()

ans = Decimal(a) * Decimal(b)

print(math.floor(ans))

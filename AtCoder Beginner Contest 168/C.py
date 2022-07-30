import math

a, b, h, m = map(int, input().split())

h %= 12
short = m*6
long = (h*60+m)/2.0

dif = abs(short-long)

rad=math.radians(dif)
ans = math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
print(ans)

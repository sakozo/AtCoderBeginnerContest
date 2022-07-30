x1, y1, x2 , y2 = map(int,input().split())

mx = x2 - x1
my = y2 - y1

x3 = x2 - my
y3 = y2 + mx

x4 = x1 - my
y4 = y1 + mx

print(x3, y3, x4, y4)
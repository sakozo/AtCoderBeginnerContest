N = int(input())
x0, y0 = map(int,input().split())
xn2,yn2 = map(int,input().split())

# 中心の座標を求める
center_x = (x0 + xn2) / 2
center_y = (y0 + yn2) / 2

# 点を移動させて、中心が原点に来るようにする
#  後の計算のための下準備
x0 -= center_x
y0 -= center_y

# 点を回転させる
from math import sin,cos,pi
x1 = cos(2*pi/N)*x0 - sin(2*pi/N)*y0
y1 = sin(2*pi/N)*x0 + cos(2*pi/N)*y0

# 原点に移動させていたため本来の位置に戻す
x1 += center_x
y1 += center_y

print(x1,y1)
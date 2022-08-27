# A = int(input())
# A, B = map(int,input().split())
# A = list(map(int,input().split()))
import math
import numpy as np

Ax, Ay = map(int,input().split())
Bx, By = map(int,input().split())
Cx, Cy = map(int,input().split())
Dx, Dy = map(int,input().split())

def cal(x0,y0,x1,y1,x2,y2):
    vec1 = [x1 - x0, y1 - y0]
    vec2 = [x2 - x0, y2 - y0]
    absvec1 = np.linalg.norm(vec1)
    absvec2 = np.linalg.norm(vec2)
    inner = np.inner(vec1, vec2)
    cos_theta = inner / (absvec1 * absvec2)
    theta = math.degrees(math.acos(cos_theta))
    return round(theta, 2)


# A=cal(Ax,Ay,Bx,By,Dx,Dy)
# B=cal(Bx,By,Ax,Ay,Cx,Cy)
# C=cal(Cx,Cy,Bx,By,Dx,Dy)
# D=cal(Dx,Dy,Ax,Ay,Cx,Cy)

# print(A)
# print(B)
# print(C)
# print(D)

DAC=cal(Ax,Ay,Cx,Cy,Dx,Dy)
BAC=cal(Ax,Ay,Cx,Cy,Bx,By)

ABD=cal(Bx,By,Ax,Ay,Dx,Dy)
CBD=cal(Bx,By,Cx,Cy,Dx,Dy)

BCA=cal(Cx,Cy,Bx,By,Ax,Ay)
DCA=cal(Cx,Cy,Dx,Dy,Ax,Ay)

CDB=cal(Dx,Dy,Cx,Cy,Bx,By)
ADB=cal(Dx,Dy,Ax,Ay,Bx,By)

# print(DAC)
# print(BAC)
# print(ABD)
# print(CBD)
# print(BCA)
# print(DCA)
# print(CDB)
# print(ADB)

sum = DAC+BAC+ABD+CBD+BCA+DCA+CDB+ADB

if 359.9 <= sum <= 360.1:
    print("Yes")
else:
    print("No")

# vec1=[Dx-Ax,Dy-Ay]
# vec2=[Bx-Ax,By-Ay]
# absvec1=np.linalg.norm(vec1)
# absvec2=np.linalg.norm(vec2)
# inner=np.inner(vec1,vec2)
# cos_theta=inner/(absvec1*absvec2)
# theta=math.degrees(math.acos(cos_theta))
# print('angle='+str(round(theta,2))+'deg')
#
#

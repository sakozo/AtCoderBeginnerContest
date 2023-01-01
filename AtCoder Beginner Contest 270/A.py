
# 1, 2, 4
A, B = map(int,input().split())

is1_A = False
is2_A = False
is3_A = False

is1_B = False
is2_B = False
is3_B = False

if A == 1 or A == 3 or A == 5 or A == 7:
    is1_A = True

if A == 2 or A == 3 or A == 6 or A == 7:
    is2_A = True

if A == 4 or A == 5 or A == 6 or A == 7:
    is3_A = True


if B == 1 or B == 3 or B == 5 or B == 7:
    is1_B = True

if B == 2 or B == 3 or B == 6 or B == 7:
    is2_B = True

if B == 4 or B == 5 or B == 6 or B == 7:
    is3_B = True

ans = 0
if is1_A or is1_B:
    ans += 1

if is2_A or is2_B:
    ans += 2

if is3_A or is3_B:
    ans += 4

print(ans)
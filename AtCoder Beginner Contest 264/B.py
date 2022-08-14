R, C = map(int,input().split())



if R == 1 or R == 15:
    ans = "black"
elif R == 2 or R == 14:
    if C == 1 or C == 15:
        ans = "black"
    else:
        ans = "white"
elif R == 3 or R == 13:
    if C == 2 or C == 14:
        ans = "white"
    else:
        ans = "black"
elif R == 4 or R == 12:
    if C == 1 or C == 15 or C == 3 or C == 13:
        ans = "black"
    else:
        ans = "white"
elif R == 5 or R == 11:
    if C == 2 or C == 4 or C == 12 or C == 14:
        ans = "white"
    else:
        ans = "black"
elif R == 6 or R == 10:
    if C == 1 or C == 15 or C == 3 or C == 13 or C == 5 or C == 10:
        ans = "black"
    else:
        ans = "white"
elif R == 7 or R == 9:
    if C == 2 or C == 4 or C == 6 or C == 10 or C == 12 or C == 14:
        ans = "white"
    else:
        ans = "black"
elif R == 8:
    if C == 1 or C == 15 or C == 3 or C == 13 or C == 5 or C == 11 or C == 7 or C == 9:
        ans = "black"
    else:
        ans = "white"

print(ans)
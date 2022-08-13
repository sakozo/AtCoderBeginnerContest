N, K = map(int, input().split())
R, S, P =  map(int, input().split())
T = list(input())

hands = []
point = 0

for i in range(N):
    if T[i] == "r":
        if i - K >= 0:
            if hands[i - K] == "p":
                hands.append("x")
                point += 0
            else:
                hands.append("p")
                point += P
        else:
            hands.append("p")
            point += P

    if T[i] == "s":
        if i - K >= 0:
            if hands[i- K] == "r":
                hands.append("x")
                point += 0
            else:
                hands.append("r")
                point += R
        else:
            hands.append("r")
            point += R

    if T[i] == "p":
        if i - K >= 0:
            if hands[i - K] == "s":
                hands.append("x")
                point += 0
            else:
                hands.append("s")
                point += S
        else:
            hands.append("s")
            point += S

print(point)
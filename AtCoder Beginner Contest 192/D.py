from collections import deque

S = int(input())
Q = int(input())

inv = False

S_deque = deque()

for i in range(len(S)):
    S_deque.append(S[i])

TFC = []

for _ in range(Q):
    TFC.append(list(input().split()))

    if TFC[0] == "1":
        if inv == False:
            inv = True
        else:
            inv = False

    else:
        F = TFC[1]
        C = TFC[2]

        if inv == False:
            if F == "1":
                S_deque.appendleft(C)
            else:
                S_deque.append(C)
        else:
            
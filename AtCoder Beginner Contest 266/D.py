N = int(input())
TXA = []

for i in range(N):
    TXA.append(list(map(int,input().split())))

end_time = TXA[N-1][0]

dp = [0]* N
position = 0
position_list = []
time_list = []
now_pisition = 0
position_list.append(now_pisition)

before_time = 0
time_list.append(before_time)
for i in range(N):

    point = 0
    txa = TXA[i]
    T = txa[0]
    X = txa[1]
    A = txa[2]

    if (T - before_time) >= abs(X - now_pisition):
        point_A = A
        now_pisition = X

    if (T - time_list[i-1]) >= abs(X - position_list[i-1]):
        point_B = A
        now_pisition = X

    if dp[i-1] + point_A >= dp[i-2] + point_B:
        before_time = T
        now_pisition = X
    else:
        before_time = T
        now_pisition = X

    dp[i] = max(dp[i-1] + point_A, dp[i-2] + point_B)

    time_list.append(before_time)
    position_list.append(now_pisition)

print(dp[N-1])
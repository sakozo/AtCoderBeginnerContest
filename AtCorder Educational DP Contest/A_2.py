N = int(input())
h_list = list(map(int, input().split()))

dp = [0] * N

dp[0] = 0
dp[1] = abs(h_list[1] - h_list[0])

for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h_list[i] - h_list[i-1]), dp[i-2] + abs(h_list[i] - h_list[i-2]))

print(dp[N-1])

N, K = map(int, input().split())
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append([A, B])

AB.sort()

village = 0
money = K
prev_a = 0
for ab in AB:
    if money - (ab[0] - prev_a) >= 0:
        money -= ab[0] - prev_a
        village = ab[0]
        money += ab[1]
        prev_a = ab[0]

if money > 0:
    village = village = prev_a + money

print(village)







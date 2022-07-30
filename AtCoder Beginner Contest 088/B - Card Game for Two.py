N = int(input())
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)

alice = 0
bob = 0

for i, card in enumerate(card_list):
    if i%2 == 0:
        alice += card
    else:
        bob += card

print(abs(alice - bob))

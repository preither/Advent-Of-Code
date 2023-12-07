cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

with open('input.txt') as f:
    c = f.readlines()

hands = []
bid = []

for i in c:
    split = i.split(" ")
    hands.append(split[0])
    bid.append(int(split[1]))

rank = {}

for i in range(len(hands)):
    card_cnt = {}
    card_val = 0
    mult = 10000000000
    for card in hands[i]:
        try:
            card_cnt[card] += 1
        except:
            card_cnt[card] = 1
        card_val += cards.index(card) * mult
        mult /= 100

    sorted_cards = dict(sorted(card_cnt.items(), key=lambda item: item[1],  reverse=True))
    try:
        f = list(sorted_cards.values())[0]
        s = list(sorted_cards.values())[1]
    except:
        pass
    if f == 5:
        card_val += 7000000000000
    elif f == 4:
        card_val += 6000000000000
    elif f == 3 and s == 2:
        card_val += 5000000000000
    elif f == 3:
        card_val += 4000000000000
    elif f == 2 and s == 2:
        card_val += 3000000000000
    elif f == 2:
        card_val += 2000000000000
    else:
        card_val += 1000000000000
    
    rank[i] = card_val

sorted_ranks = dict(sorted(rank.items(), key=lambda item: item[1]))

winnings= 0
r = 1
for key in sorted_ranks:
    winnings += bid[key] * r
    r += 1

print(winnings)

from itertools import combinations
NM = list(input().split())
N = int(NM[0])
M = int(NM[1])
card = list(input().split())
for i in range(len(card)) :
    card[i] = int(card[i])

for j in card :
    if j > M :
        card.remove(j)

cardCom = list(combinations(card,3))
cardSum = []

for k in cardCom :
    cardSum += [sum(k)]

result = -1

for r in cardSum :
    if r <= M :
        if M - result > M - r :
            result = r

print(result)
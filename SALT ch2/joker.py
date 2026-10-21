n, m = [int(x) for x in input().split()]
cards = input()
values = "*A23456789TJQK"
card_vals = []

for i in range(n):
    if values.index(cards[i]) > 10:
        val = 10
    else:
        val = values.index(cards[i])

    card_vals.append(val)

asterisks = cards.count('*')

if sum(card_vals) > m or (sum(card_vals) == m and asterisks >= 1) or (sum(card_vals) + asterisks) > m:
    print("NO")

elif sum(card_vals) + asterisks * 10 >= m:
    print("YES")

    if sum(card_vals) == m:
        print(cards)
    else:
        for i in range(n): #this sets all asterisks to 1
            if cards[i] != "*":
                continue
            else:
                card_vals[i] = 1

        for i in range(n):
            while sum(card_vals) < m:
                if cards[i] != "*":
                    break
                elif card_vals[i] == 10:
                    break
                else:
                    card_vals[i] += 1

        new_cards = []
        for i in range(n):
            if cards[i] != '*':
                new_cards.append(cards[i])
            else:
                new_cards.append(values[card_vals[i]])
        
        print("".join(new_cards))

else:
    print("NO")
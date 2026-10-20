n = int(input())
skill = [int(x) for x in input().split()]
winners = skill.copy()
rounds = [0 for _ in range(n)]
is_win = [True for _ in range(n)]

while is_win.count(True) != 1:
    for i in range(0, len(winners), 2): 
        p1 = winners[i]
        p2 = winners[i+1]

        rounds[skill.index(p1)] += 1
        rounds[skill.index(p2)] += 1

        if p1 > p2:
            is_win[skill.index(p2)] = False
        elif winners[i+1] > winners[i]:
            is_win[skill.index(p1)] = False
        
    winners = []
    for i in range(n):
        if is_win[i] == True:
            winners.append(skill[i])

rounds[skill.index(winners[0])] = "CHAMP"
print(*rounds)
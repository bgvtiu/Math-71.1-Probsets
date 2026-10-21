w = input()
p = input().split()

elim = []
rounds = 0
has_won = False

while has_won is False and len(p) > 0:
    rounds += 1
    guess = input().split()
    correct = [True for _ in range(len(guess))]
    penalty = [0 for _ in range(len(guess))]

    for g in range(len(guess)):
        for i in range(len(w)):
            if guess[g][i] != w[i]:  
                penalty[g] += 1

        for i in range(len(w)):
            if guess[g][i] != w[i]:  
                correct[g] = False
                break

    if correct.count(True) == 0:
        to_elim = penalty.index(max(penalty))
        elim.append(p[to_elim])
        p.pop(to_elim)
    else: has_won = True

if rounds == 1 and has_won == True:
    print("none eliminated")
    print(p[correct.index(True)])
elif has_won is False:
    print(*elim)
    print("no winner")
elif has_won == True:
    print(*elim)
    print(p[correct.index(True)])
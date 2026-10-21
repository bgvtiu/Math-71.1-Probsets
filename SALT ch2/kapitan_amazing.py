keys = input() + input() + input()
n = int(input())
passwords = [input() for _ in range(n)]

asterisks = keys.count('*')
results = []

for p in passwords:
    possible = True
    for i in range(len(keys)):
        if keys[i] in p:
            possible = False
            break

        if len(set(p)) != asterisks:
            possible = False

    results.append(possible)

for r in results:
    if r:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
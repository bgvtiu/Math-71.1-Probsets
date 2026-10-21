s = input()
t = input()

possible = True
for i in range(len(s)):
    if t[i] == '.' or t[i] == "^": 
        continue
    elif t[i] == s[i]: 
        continue
    else:
        possible = False
        break

if possible:
    print("Yes")

    cursor = t.index("^")
    solution = []
    for i in range(cursor, len(s)):
        if t[i] == t[i] == '.' or t[i] == "^":
            solution.append(s[i])

    if cursor != 0:
        for i in range(0, cursor):
            if t[i] == t[i] == '.':
                solution.append(s[i])

    print("".join(solution))

else:
    print("No")
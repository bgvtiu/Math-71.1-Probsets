n = int(input())
w = [int(x) for x in input().split()]
m = int(input())

for _ in range(m):
    l, r, x = [int(x) for x in input().split()]

    wowed = False
    for i in range(l-1, r):
        if i == l-1: #skips shecking the first day
            continue
        elif w[i] - w[i-1] >= x: 
            wowed = True
            break

    if wowed:
        print("Wow")
    else:
        print("Edi wow")
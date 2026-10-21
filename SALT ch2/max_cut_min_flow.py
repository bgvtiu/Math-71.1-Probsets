n, b = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
complete = 0

maxi = max(x)

if maxi > 0:
    for cost in x:
        if cost > 0:
            b += cost
    print(b)
elif maxi + b >= 0:
    b += maxi
    print(b)
else:
    print(-1)
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    l, r, x = [int(x) for x in input().split()]

    for i in range(l-1, r):
        buy_date = -1
        if a[i] >= x:
            buy_date = i+1
            break
    print(buy_date)
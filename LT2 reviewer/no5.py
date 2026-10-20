n, m, l, r = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]

x.insert(0, 0)
y.insert(0, 0)

counter = 0
for a in range(1, n+1):
    for b in range(1, m+1):
        area = (x[a] - x[a-1]) * (y[b] - y[b-1]) #length * width = area
        if area >= l and area <= r:
            counter += 1

print(counter)
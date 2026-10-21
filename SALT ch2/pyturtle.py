def move(x, d):
    global dir
    for _ in range(x):
        dir.append(d)

n = int(input())
a = [int(x) for x in input().split()]
dir = []

for i in range(n):
    if i == 0:
        move(a[i], "U")
    else:
        if a[i] - a[i-1] < 0:
            move(a[i-1] - a[i], "D")
        if a[i] - a[i-1] > 0:
            move(a[i] - a[i-1], "U")
    dir.append("R")

move(a[-1], "D")
move(n, "L")

print("".join(dir))
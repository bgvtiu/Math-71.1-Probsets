s = input()

counter = 0
while s != "42" and s != "1":
    result = 0
    for digit in s:
        result += int(digit)**2

    s = str(result)
    counter += 1

print(counter)
print(s)
n = int(input())
prices = [int(x) for x in input().split()]
years = [int(x) for x in input().split()]

sum = 0
for i in range(n):
    if years[i] <= 1960:
        continue
    elif years[i] < 2000:
        sum += prices[i] * 1.105**(2024-years[i])
    else:
        sum += prices[i] / 2


print(f"{sum:.2f}")
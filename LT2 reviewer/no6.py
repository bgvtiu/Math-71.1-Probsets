stations = (
    "North Avenue",
    "Quezon Avenue",
    "GMA-Kamuning",
    "Araneta Center-Cubao",
    "Santolan-Annapolis",
    "Ortigas",
    "Shaw Boulevard",
    "Boni",
    "Guadalupe",
    "Buendia",
    "Ayala",
    "Magallanes",
)

on = [int(x) for x in input().split()]
off = [int(x) for x in input().split()]

p = 0
breaking = 0
for i in range(len(stations)):
    p += on[i] - off[i]

    if p >= 30:
        breaking += 1
    else: breaking = 0

    if breaking == 2:
        print(stations[i])
        break

if breaking < 2:
    print("Taft Avenue")
print(p)
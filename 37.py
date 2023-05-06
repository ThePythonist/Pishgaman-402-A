items = [
    11,
    4,
    6,
    3,
    12,
    14,
    5
]

print(items)

evens = []

for i in items:
    if i % 2 == 0:
        # evens.append(i)
        evens += [i]

print("Evens are : ")
print(evens)

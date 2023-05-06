items = [12, True, "Shiraz", 6.6, 9, (), False, {}, 4.3]
numbers = []

for i in items :
    if type(i) == str:
        numbers.append(i)

print(numbers)

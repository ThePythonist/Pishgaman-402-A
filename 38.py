items = [12, True, "Shiraz", 6.6, 9, (), False, {}, 4.3]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)

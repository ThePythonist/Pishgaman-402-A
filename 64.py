def status(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# print(status(16))

numbers = [12, 3, 5, 6, 7, 14, 20]

for n in numbers:
    print(status(n))

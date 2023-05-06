items = [1, 2, 3, 4, 5]

# for i in range(5):
#     x = int(input("Enter numbers (6-10) : "))
#     if 5 < x < 11:
#         items.append(x)
#
# print(items)

while not len(items) == 10:
    x = int(input("Enter numbers (6-10) : "))
    if 5 < x < 11:
        items.append(x)
    else :
        print("Invalid Number (Only 6-10)")

print(items)

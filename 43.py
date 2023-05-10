items1 = ["maserati", "bmw", "saipa", "ford"]
items2 = ["saipa", "kerman motor", "bmw", "volvo"]
common = []

# for i in items1:
#     if i in items2:
#         common.append(i)
#
# print(common)

for i in items1:
    for j in items2:
        if i == j:
            common.append(i)
print(common)

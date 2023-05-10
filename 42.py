tedad = int(input("Chand adad niaz darid : "))
items = []

for i in range(tedad):
    print("Adad", i + 1, "vared konid : ", end="")
    x = float(input())
    items.append(x)

print("Maximum :", max(items))

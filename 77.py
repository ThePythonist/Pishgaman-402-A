# x = int(input("Enter x : "))
# y = int(input("Enter y : "))

compare = lambda x, y: "Equal" if x == y else "First is bigger" if x > y else "Second is bigger"
print(compare(32, 32))

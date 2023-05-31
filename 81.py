a = int(input("Enter integer part : "))
b = int(input("Enter decimal part : "))
# number = "{a}.{b}".format(a=a, b=b)
number = f"{a}.{b}"
print(float(number))

def func(x, y):
    numbers = range(x, y)
    # print(list(numbers))
    print(*numbers)


x = int(input("Range start : "))
y = int(input("Range end : "))
func(x, y)

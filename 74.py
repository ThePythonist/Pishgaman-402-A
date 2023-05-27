def func(x, y):
    if y == 1:
        return x
    else:
        return x * func(x, y - 1)


print(func(5, 3))

# Or :
# def func(x, y, counter):
#     if counter == y:
#         return x
#     else:
#         return x * func(x, y, counter + 1)
#
#
# print(func(5, 4, 1))

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)


factorial = lambda n: n if n == 1 else n * factorial(n - 1)
print(factorial(5))

def numbers(items):
    # n = []
    # for i in items:
    #     if type(i) in [int, float]:
    #         n.append(i)
    numbers = [i for i in items if type(i) in [int, float]]
    return numbers


items = [4, True, 12.5, 6.3, "Metallica", 7]
print(numbers(items))

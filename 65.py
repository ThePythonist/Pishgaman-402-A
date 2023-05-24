# def mysort(items=[]):
#     items.sort()
#     return items[::-1]
#
#
# items = [14, 2, 3, -3, 5, 1, 4, -1]
# print(mysort(items))

def mysort(items=[]):
    items.sort(reverse=True)
    return items


items = [14, 2, 3, -3, 5, 1, 4, -1]
print(mysort(items))

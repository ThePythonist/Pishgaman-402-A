# def check(word):
#     if len(word) == len(set(word)):
#         print("Tekrari Nadarad")
#     else:
#         print("Tekrari Darad")
#
#
# check(input("Enter any word : "))

def check(word):
    lst = []

    for i in word:
        if i not in lst:
            lst.append(i)
        else:
            print("Harf", i, "Tekrari ast")

    if len(lst) == len(word):
        print("Tekrari nadasht")


check("mohammad")

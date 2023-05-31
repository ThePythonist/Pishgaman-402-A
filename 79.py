# def check(word):
#     if len(word) == len(set(word)):
#         print("Tekrari Nadarad")
#     else:
#         print("Tekrari Darad")
#
#
# check(input("Enter any word : "))

check = lambda word: False if len(word) == len(set(word)) else True
print(check(input("Tekrari darad ya na : ")))

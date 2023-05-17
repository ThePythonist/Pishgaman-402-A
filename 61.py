word = "python"
indexes = {}
count = 0

for i in word :
	indexes.setdefault(i,count)
	count += 1

print(indexes)

#----------------------------------------

# word = "Engineer"

# d = {}
# for i in range(len(word)):
#     d.setdefault(i, word[i])

# d = dict(zip(range(len(word)), word))
# print(d)

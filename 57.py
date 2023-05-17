scores = {
	"riazi1":17,
	"mabani computer":20,
	"madar haye manteghi":16,
	"zaban omomi":18,
	"fizik1":9,
	"andishe eslami":13
}

for k,v in scores.items():
	if v >= 10:
		print(k,": Passed")
	else:
		print(k,": Failed")

print()

GPA = sum(scores.values()) / len(scores)
print("Moadel :",GPA)

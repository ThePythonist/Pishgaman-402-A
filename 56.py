ages = {
	"Mina":19,
	"Parham":31,
	"Reza":16,
	"Mayram":23
}

oldest = max(ages.values())

for i in ages:
	if ages[i] == oldest:
		print(i,":",ages[i])

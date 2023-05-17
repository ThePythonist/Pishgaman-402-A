info = {
	"name":"mohammad",
	"age":27,
	"job":"Civil Engineer",
	"city":"esfahan",
	"emp_id":"453456"
}

while True:
	entry = input("Enter any key to search in info : ")

	if entry in info.keys():
		print("Found :",info[entry])
		break
	else :
		print("Not Found.")

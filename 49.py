n = int(input("Enter any number : "))
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors)

if len(divisors) == 2 :
    print("The number is prime")
else :
    print("The number is not prime")

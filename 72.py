def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


while True:
    entry = input("Enter any number : ")
    try:
        entry = int(entry)
        try:
            print(factorial(entry))
            if input("Try again ? ") == "yes":
                pass
            else:
                break
        except RecursionError:
            print("Number must be larger than 0")
    except ValueError:
        print("Entry must be a integer number")

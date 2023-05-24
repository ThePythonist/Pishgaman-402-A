# def prime_check(n):
#     divisors = [i for i in range(1, n + 1) if n % i == 0]
#     print("Prime") if len(divisors) == 2 else print("Not Prime")
#
#
# prime_check(int(input("Enter any number : ")))

def prime_check(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return True if len(divisors) == 2 else False


print(prime_check(int(input("Enter any number : "))))

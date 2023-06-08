def main():
    def register():
        username = input("Type your username : ").lower()
        password = input("Type your password : ")

        open("users.txt", "a+").write(username + "\n")
        open("passwords.txt", "a+").write(password + "\n")
        print(f"Signed up user {username}")

    def login():
        users = [i[:-1] for i in open("users.txt").readlines()]
        passwords = [i[:-1] for i in open("passwords.txt").readlines()]
        accounts = dict(zip(users, passwords))
        print(accounts)

        username = input("Type your username : ").lower()
        password = input("Type your password : ")

        if username in accounts:
            if password == accounts[username]:
                print("Successfully logged in")
            else:
                print("Password is wrong")
                login()
        else:
            print("Account not found")
            login()

    operation = input("""
Choose an operation :
1 : Register
2 : Login to your account
""")

    if operation == "1":
        register()
    elif operation == "2":
        login()
    else:
        print("Invalid entry. Choose 1 or 2")
        main()


main()

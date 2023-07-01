from Models import User


class Admin(User):
    def __init__(self, us, pw, delete_user):
        super().__init__(us, pw)
        self.delete_user = delete_user


admin = Admin("admin", "123", True)
admin.login()
print(admin.delete_user)

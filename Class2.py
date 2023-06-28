# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()

class Father:
    def __init__(self, fname, address, job):
        self.familyname = fname
        self.address = address
        self.job = job

        def say_hello(self):
            print("Hello")


class Child(Father):
    def __init__(self, fname, address, uni, job=None):
        super().__init__(fname, address, job)
        self.university = uni

    def say_goodbye(self):
        print("Goodbye")


# pedar = Father("Ahmadi", "Tehran, Ekbatan, Varzesh St", "Teacher")
farzand = Child("Ahmadi", "Tehran, Ekbatan, Varzesh St", "Tehran University")
print(farzand.university)
print(farzand.job)

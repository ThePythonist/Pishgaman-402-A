print(__name__)

def power(a,b):
    print(a**b)

def f1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    longest = max(lengths)

    for i in text:
        if len(i) == longest:
            return i


def f2(text):
    text = text.split()
    text.sort(key=len)
    return text[-1]


def f3(text):
    text = text.split()
    return max(text, key=len)

if __name__ == "__main__":
    print("You are using mymymodule as main program")
else :
    print("You are using mymodule as a module")



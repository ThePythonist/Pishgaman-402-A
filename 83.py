def f1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    longest = max(lengths)

    for i in text:
        if len(i) == longest:
            return i


# print(f1("python is a good programming language"))


def f2(text):
    text = text.split()
    text.sort(key=len)
    return text[-1]


# print(f2("python is 1 good programming language"))

def f3(text):
    text = text.split()
    return max(text, key=len)


print(f3("python is 1 good programming language"))

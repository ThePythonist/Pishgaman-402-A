def show_jalali_age(year):
    import jdatetime
    today = str(jdatetime.datetime.now())
    thisyear = int(today.split()[0].split("-")[0])
    age = thisyear - year
    print(age)


# show_jalali_age(1370)


def show_gregorian_age(year):
    import datetime
    today = str(datetime.datetime.now())
    thisyear = int(today.split()[0].split("-")[0])
    age = thisyear - year
    print(age)


# show_gregorian_age()

if input("""
Choose an option : 
1 : Gregorian age
2 : Shamsi age
""") == "1":
    show_gregorian_age(int(input("Enter your birth year : ")))
else:
    show_jalali_age(int(input("Enter your birth year : ")))

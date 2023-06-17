from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

today = str(JalaliDate.today()).split("-")
today = [int(i) for i in today]
date = JalaliDateTime(today[0], today[1], today[2], 19, 22, 10, 0, pytz.utc).strftime("%A")
# print(date.split()[0])
print(date)

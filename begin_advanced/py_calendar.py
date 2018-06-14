
#py_calendar.py
import calendar

#create a TextCalendar instance
cal = calendar.TextCalendar()
print("We just produced a {}.\n".format(type(cal)))

print("Let's check out the calendar for April, 2016\n")

calendar.prmonth(2016,4)
print()

#what day of the week was I born?
birthday_year=1957
birthday_month=5
birthday_day=10

birthday_day_of_week=calendar.weekday(birthday_year,
                                      birthday_month,
                                      birthday_day)

birthday_dict={0:'Mon', 1:'Tue', 2:'Wed', 3:'Thur', 4:'Fri', 5:'Sat', 6:'Sun'}
print("I was born on a {}".format(birthday_dict[birthday_day_of_week]))

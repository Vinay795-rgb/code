#  Write  a program to print the calendar of any given year

import calendar
y = int(input("Enter the year : "))
m = 1
print("\n***********CALENDAR*******")
cal = calendar.TextCalendar(calendar.SUNDAY)
#  An instance of TextCalendar class is created and calendar. SUNDAY means that you want to start dis[playing the calendar from SUNDAY
i=1
while i<=12:
          cal.prmonth(y,i)
          i+=1
#  Prmonth() is a function of the class that print the calendar for given month and year
import calendar

year = int(input('enter a year: '))
month = int(input('enter a month: '))

cal = calendar.month(year,month)
print(cal)

year = 1901
if year % 4 == 0 and and year % 100 != 0 or year % 400 == 0:
  leap = True
  feb = 29
else:
  leap = False
  feb = 28

  daysInMonth = {31,feb,31,30,31,30,31,31,30,31,30,31}

  for i in daysInMonth:
    print(i)

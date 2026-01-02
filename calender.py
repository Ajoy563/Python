import calendar
y=int(input("Enter a Year: "))
for month in range(1,13):
    mycal=calendar.monthcalendar(y,month)
    week1=mycal[0]
    week2=mycal[1]
    if(week1[calendar.MONDAY] != 0):
        a=week1[calendar.MONDAY]
    else:
        a=week2[calendar.MONDAY]
    print(calendar.month_name[month],a)
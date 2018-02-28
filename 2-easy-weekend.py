import datetime

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

today = days[datetime.datetime.weekday(datetime.datetime.now())]
timeWithoutMicro = str(datetime.datetime.time(datetime.datetime.now())).split(".")
time = str(timeWithoutMicro[0]).split(":")

for i, day in enumerate(days):
	if day == today:
		days_left = 4 - i

hoursLeftToday = 17 - int(time[0])
hoursLeftTotal = hoursLeftToday + 9 * days_left

print "The day is %s and the time is %s." % (today,timeWithoutMicro[0])
print "You have %s days until the weekend, %s work hours and %s non-work hours to go. " % (days_left,hoursLeftTotal,((days_left * 24) - (9 * days_left)))
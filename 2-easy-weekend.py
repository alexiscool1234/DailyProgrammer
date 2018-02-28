# import datetime

# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# today = days[datetime.datetime.weekday(datetime.datetime.now())]
# timeWithoutMicro = str(datetime.datetime.time(datetime.datetime.now())).split(".")
# time = str(timeWithoutMicro[0]).split(":")

# for i, day in enumerate(days):
	# if day == today:
		# days_left = 4 - i

# hoursLeftToday = 17 - int(time[0])
# hoursLeftTotal = hoursLeftToday + 9 * days_left

# print "The day is %s and the time is %s." % (today,timeWithoutMicro[0])
# print "You have %s days until the weekend, %s work hours and %s non-work hours to go. " % (days_left,hoursLeftTotal,((days_left * 24) - (9 * days_left)))



import datetime

delta = 1
dayCounter = 0
today = datetime.datetime.now()
today.strftime("%X") # time in HH:MM:SS

hoursBeforeTomorrow = 24 - int(str(today.strftime("%X")).split(":")[0])
minsLeftToday = (hoursBeforeTomorrow * 60) - int(str(today.strftime("%X")).split(":")[1])

print "Hours left until hometime today: %s" % round((float((float(minsLeftToday )) / 60) - 7), 2)

while True:
	if str((today + datetime.timedelta(delta)).strftime("%A")) != "Friday":
		delta += 1
		dayCounter += 1
	else:
		break
		
if dayCounter != 0:
	print "Hours left until weekened: %s" % (round((float((float(minsLeftToday)) / 60)), 2) + ((dayCounter) * 24) + 17)
else:
	print "Hours left until weekened: %s" % (round((float((float(minsLeftToday)) / 60)), 2) + 7)

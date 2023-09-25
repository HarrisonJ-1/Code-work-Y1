#Hours per week

hourspernight = int(input("How many hours per night do you sleep? "))

hoursperweek = hourspernight * 7

print ("You sleep",hoursperweek,"hours per week")

#Hours per month

hourspermonth = float(hoursperweek) * 4.35

print ("You sleep",hourspermonth,"hours per month")

#Days slept per month
dayspermonth = float(hourspermonth) / 24

print ("This equates to",dayspermonth,"days per month")
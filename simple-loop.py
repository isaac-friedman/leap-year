import datetime

def is_leap(year):
	leap = False
	if year % 4 != 0:
		return leap
	leap = True
	if (year % 100 == 0) and (year % 400 != 0):
		leap = False
	return leap

#gets current year from system so program will be valid as long as we use the Gregorian calendar
year = datetime.datetime.now().year
leap_count = 0
while leap_count < 20:
	if is_leap(year):
		leap_count += 1
		print(year)
	year += 1
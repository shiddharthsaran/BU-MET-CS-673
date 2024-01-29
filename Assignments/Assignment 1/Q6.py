def find_leap_year(current_year):
	if current_year % 4 == 0:
		if current_year % 100 == 0:
			if current_year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


if __name__ == '__main__':
	usr_inp = int(input('Enter a year:'))
	if find_leap_year(usr_inp):
		print(f'Year {usr_inp} is a leap year.')
	else:
		print(f'Year {usr_inp} is not a leap year.')

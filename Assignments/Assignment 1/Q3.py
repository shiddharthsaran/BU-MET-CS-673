def check_str_palindrome(str):
	if str == str[::-1]:
		res = f'The string {str} is a palindrome.'
	else:
		res = f'The string {str} is not a palindrome.'
	return res


if __name__ == '__main__':
	while True:
		usr_inp = input('Enter a string:').lower().strip()
		if usr_inp == 'q':
			break
		else:
			palin_res = check_str_palindrome(usr_inp)
			print(palin_res)
			break

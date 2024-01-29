def print_multiplication_table(start, end):
	for row in range(start, end + 1):
		for col in range(start, end + 1):
			print(row * col, end='\t')
		print()


if __name__ == '__main__':
	start_rage = 1
	end_range = 12
	print_multiplication_table(start_rage, end_range)

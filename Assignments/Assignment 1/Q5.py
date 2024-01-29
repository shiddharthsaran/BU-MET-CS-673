def compute_fibonacci_nums(end):
	prev_num = 1
	curr_num = 1
	start = 3
	print(f'1:{prev_num}')
	print(f'2:{curr_num}')
	while start < end + 1:
		next_num = prev_num + curr_num
		print(f'{start}:{next_num}')
		prev_num = curr_num
		curr_num = next_num
		start += 1


if __name__ == '__main__':
	end_range = 100
	compute_fibonacci_nums(end_range)
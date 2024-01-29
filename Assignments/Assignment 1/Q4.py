def get_list_inp(lst_name):
	return input(f'Enter elements for {lst_name} separated by comma(,'
						  '):').lower().strip().split(',')


def combine_list(lst_1, lst_2):
	combined_lst = list()
	for ele_1, ele_2 in zip(lst_1, lst_2):
		combined_lst.append(ele_1)
		combined_lst.append(ele_2)
	return combined_lst


if __name__ == '__main__':
	while True:
		usr_lst_1 = get_list_inp('list 1')
		usr_lst_2 = get_list_inp('list 2')
		if len(usr_lst_1) != len(usr_lst_2):
			print('The two lists are not of the same length.')
			continue
		else:
			res_lst = combine_list(usr_lst_1, usr_lst_2)
			print(f'Combined List Result:{res_lst}')
			break

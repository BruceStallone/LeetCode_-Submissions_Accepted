def insert_sort(li):
	for i in range(1, len(li)):
		sorted_num = i - 1
		temp = li[i]
		while sorted_num >= 0 and li[sorted_num] > temp:
			li[sorted_num + 1] = li[sorted_num]
			sorted_num -= 1
		li[sorted_num + 1] = temp
	return li


def count_sort(li, max_count=100):
	count = [0 for _ in range(max_count+1)]	#建立一个记录每个数字出现多少次的列表
	for val in li:
		count[val] += 1 #每个数字出现一次，就在对应的数字（排位顺序）+1
	li.clear()
	for ind, val in enumerate(count):
		for i in range(val):	
			li.append(ind)
	# 通过循环来排序，每个数字（位置编号IND）出现了多少次（val），就加val次的ind
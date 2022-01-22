def redix_sort(li):
	max_num = max(li)
	ite_num = 0
	while 10**ite_num <= max_num:	#根据最大数的位数控制循环迭代多少次
		buckets = [[] for _ in range(10)]
		for val in li:
			digit = (var//10**ite_num) % 10
			buckets[digit].append(val)
		li.clear()
		for bucket in buckets:
			li.extend(bucket)
		ite_num += 1

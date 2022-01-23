def bucket_sort(li, n=100, max_num=10000):
	buckets = [[] for _ in range(n)] #创建若干个空桶
	for var in li:
		i = min(var // (max_num // n), n - 1) #表示var放到几号桶,为了防止越界，用了min来控制
		buckets[i].append(var)
		#下面紧跟每个桶内的排序
		for j in range(len(buckets[i]-1, 0, -1)):
			if buckets[i][j] < buckets[i][j-1]:
				buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
			else:
				break
	sort_li= []
	for bucket in buckets:
		sort_li.extend(bucket)
	return sort_li
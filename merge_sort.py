def merge(li, low, mid, high):
	"""
	归并两个列表，从小到大排列
	"""
	i = low
	j = mid + 1
	ltmp = []
	while i <= mid and j <= high:    #只要左右两边都有数
		if li[i] < li[j]:
			ltmp.append(li[i])
			i += 1
		else:
			ltmp.append(li[j])
			j += 1
	#while执行完毕，有一组没数，一组还有数
	while i <= mid:
		ltmp.append(li[i])
		i += 1
	while j <= high:
		ltmp.append(li[j])
		j += 1
	#把剩下的数都处理完了
	li[low:high + 1] = ltmp


def merge_sort(li, low, high):
	"""拆分成单独元素,然后合并"""
	if low < high:    #至少有两个元素，开始递归
		mid = (low + high) // 2
		merge_sort(li, low, mid)
		merge_sort(li, mid+1, high)
		merge(li, low , mid, high)
	return li



def partition(li, left, right):
	tmp = li[left]    #从最左边第一个抽出1个数，作为分隔数
	while left < right:    #当左边界一直小于右边界
		while left < right and li[right] >= tmp:    #右边的数一直大于分隔数时
			right -= 1    #右边界左移
		li[left] = li[right]   #当右边的数小于分隔数时，插到左边的区域
		while left < right and li[left] <= tmp:    #左边的数一直小于分隔数时
			left += 1    #左边界右移
		li[right] = li[left]    #当左边的数大于分隔数时，插到右边区域
	li[left] = tmp
	return left

def quick_sort(li, left, right):
	if left < right:
		mid = partition(li, left, right)
		quick_sort(li, left, mid - 1)
		quick_sort(li, mid + 1, right)

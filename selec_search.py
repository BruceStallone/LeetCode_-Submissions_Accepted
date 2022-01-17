def select_search(li):
	list_new = []
	for i in range(len(li)):
		min_val = min(li)
		list_new.append(min_val)
		li.remove(min_val)
	return(list_new)


def select_sort(li):
	for i in range(len(li)-1):
		min_loc = li[i]
		for j in range(i+1, len(li)):
			if li[j] < li[min_loc]:
				min_loc = j
		if min_loc != i:
			li[i], li[min_loc] = li[min_loc], li[i]
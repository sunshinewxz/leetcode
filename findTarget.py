def findTarget(array, target):
	left, right = 0, len(array)-1
	index = -1
	while(left <= right):
		mid = (left + right) // 2
		if array[mid] >= target:
			if index == -1:
				index = mid
			else:
				index = min(index, mid)
			right = mid - 1
		else:
			left = mid + 1
	return index

array = [1,2,3,4,5]
print(findTarget(array, 8))

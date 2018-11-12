def merge(matrix):
	index = 0
	result = []
	list_num = len(matrix)
	while(len(matrix) > 0):
		for i,m in enumerate(matrix):
			result.append(m.pop(0))
			if len(m) == 0:
				matrix.pop(i)
	return result

matrix = [[0, 1], [2, 3, 4, 5], [6]]
print(merge(matrix))

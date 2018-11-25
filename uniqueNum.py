def uniqueNum(input_str):
	if len(input_str) == 0:
		return 0
	prechar = input_str[0]
	stack = []
	index = 0
	length = 0
	while(index < len(input_str)):
		first_index = index
		prechar = input_str[index]
		length = 0
		while(index < len(input_str) and input_str[index] == prechar):
			length += 1
			index += 1
		if len(stack) == 0:
			stack.append([input_str[first_index], length, first_index])
		elif stack[-1][1] < length:
			stack.pop()
			stack.append([input_str[first_index], length, first_index])
	return stack[-1][2]


input_str = 'aabbbbbc'
print(uniqueNum(input_str))
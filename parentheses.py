def parentheses(inputs):
	if len(inputs) == 0:
		return
	stack = []
	result = ''
	for i, char in enumerate(inputs):
		if char == '(':
			if len(stack) > 0 and not ('a' <= inputs[i-1] <= 'z'):
				index = stack[0][1]
			else:
				index = len(result)
			stack.append([char,index])
		elif char == ')':
			if len(stack) > 0:
				_,index = stack.pop()
				result = result[0:index] + '0' + result[index:] + '0'
			else:
				result += '-1'
		else:
			result += char
	while(len(stack) > 0):
		_,index = stack.pop()
		result = result[:index] + '1' + result[index:]
	return result

inputs = '((abc))((cde)'
print(parentheses(inputs))
inputs = '((abc))))'
print(parentheses(inputs))
inputs = '((c(de)'
print(parentheses(inputs))
inputs = '(abc)(cde)'
print(parentheses(inputs))
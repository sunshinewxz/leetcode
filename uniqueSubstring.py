def uniqueSubstring(input_str, k):
	print(input_str)
	result = set()
	for i in range(len(input_str)-k+1):
		result.add(input_str[i:i+k])

	result = sorted(list(result))
	return result

a = 'caaab'
print(uniqueSubstring(a, 2))



# if the substring can be incontinuous
def uniqueSubstring(input_str, k):
	print(input_str)
	result = set()

	def backtrack(temp, sub):
		if len(temp) == k:
			result.add(temp)
			return
		for i in range(len(sub)):
			temp = temp + sub[i]
			backtrack(temp, sub[i+1:])
			temp = temp[:-1]

	backtrack('', input_str)
	result = sorted(list(result))
	return result
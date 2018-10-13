class Solution():
	# solution 1
	# def deleteDuplicate(self, input_s):
	# 	queue = []
	# 	input_s = list(input_s)
	# 	for i in range(len(input_s)):
	# 		if queue and queue[len(queue)-1] == input_s[i]:
	# 			queue.pop()
	# 		else:
	# 			queue.append(input_s[i])
	# 	return "".join(queue)

	# follow up: space: O(1)
	def deleteDuplicate(self, input_s):
		input_s = list(input_s)
		i = 1
		while(i < len(input_s)):
			if i > 0 and input_s[i] == input_s[i-1]:
				input_s.pop(i-1)
				input_s.pop(i-1)
				i = i - 1
			else:
				i = i + 1
		return "".join(input_s)

s = Solution()
input_s = "abbaedf"
print(s.deleteDuplicate(input_s))

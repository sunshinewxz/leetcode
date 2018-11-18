def deleteSame(input_str):
	if len(input_str) == 0:
		return input_str
	stack = []
	i = 0
	while(i < len(input_str)):
		if len(stack) == 0:
			stack.append(input_str[i])
			i += 1
			continue
		if input_str[i] == stack[-1]:
			stack.pop()
			i += 1
		else:
			stack.append(input_str[i])
			i += 1
	return "".join(stack)

input_str = 'abbaedf'
print(deleteSame(input_str))

'''
follow up
space complexity: O(1)
'''
import collections
def deleteSame_follow_up(input_str):
	if len(input_str) == 0:
		return input_str
	stack = collections.defaultdict(list)
	i = 0
	index = 0
	while(i < len(input_str)):
		if input_str[i] not in stack:
			stack[input_str[i]] = [i]
			i += 1
			index = 0
			continue
		if len(stack[input_str[i]]) > 0 and i == stack[input_str[i]][-1]+index+1:
			stack[input_str[i]].pop()
			index += 2
			if len(stack[input_str[i]]) == 0:
				del stack[input_str[i]]
			i += 1
		else:
			stack[input_str[i]].append(i)
			index = 0
			i += 1
	stack = sorted(stack.items(), key=lambda v:v[1])
	result = [k[0] for k in stack]
	return "".join(result)

input_str = 'aabbaceedf'
print(deleteSame_follow_up(input_str))
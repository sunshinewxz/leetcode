# Question 1
# class food(object):
# 	def __init__():
# 		self.memo = []

# class findIngredient(foodlist):
# 	ingredient = set()
# 	for food in foodlist:
# 		for sub in food:
# 			if isinstance(sub, food):
# 				for i in sub.memo:
# 					ingredient.add(i)
# 			else:
# 				ingredient.add(sub)
# 	return list(ingredient)

# Question 2
def combination(strlist):
	if len(strlist) == 0:
		return
	def bfs(stack, index):
		if index == len(strlist):
			return stack
		stack_num = len(stack)
		for i in range(stack_num):
			ele = stack.pop(0)
			for j,char in enumerate(strlist[index]):
				stack.append(ele + [char])
		return bfs(stack, index+1)


	stack = [[i] for i in strlist[0]]
	return bfs(stack, 1)


strlist = [['1','2','3'], ['a','b','c'], ['d','e','f']]
print(len(combination(strlist)))
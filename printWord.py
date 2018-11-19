def printWord(num):
	l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	l2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen','seventeen', 'eighteen', 'ninteen']
	l3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
	l4 = 'one hundred'
	result = ''
	# while(num != 0):
	temp = num//100
	num = int(num % 100)
	# num == 100
	if temp == 1:
		return l4
	temp = num//10
	num = int(num % 10)
	# num > 20
	if temp >= 2 and num == 0:
		return l3[temp-2]
	if temp >= 2:
		result += l3[temp-2] + ' ' + l1[num]
		return result
	# num > 10
	if temp >= 1:
		result += l2[num]
		return result
	# num > 0
	if temp == 0:
		result += l1[num]
		return result

def createWord():
	for i in range(1, 101):
		print(printWord(i))

createWord()

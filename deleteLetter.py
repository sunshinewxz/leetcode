def deleteLetter(input_str):
    stack = []
    for i,char in enumerate(input_str):
        if len(stack) == 0:
            stack.append([char, 1])
            continue
        if char == stack[-1][0]:
            stack[-1][1] += 1
        elif ord(char) - ord(stack[-1][0]) == 1 or ord(char) - ord(stack[-1][0]) == -1:
            stack.pop()
        else:
            stack.append([char, 1])
    print(stack)
    return "".join(stack[i][0]*stack[i][1] for i in range(len(stack)))

input_str = 'aadbcce'
print(deleteLetter(input_str))

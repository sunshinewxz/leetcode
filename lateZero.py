def lateZero(input_str):
    left, right = 0, len(input_str)-1
    while(left < len(input_str)):
        if input_str[left] == 0:
            input_str = input_str[:left]+input_str[left+1:]+[0]
            if left == len(input_str)-1:
                return input_str
            if input_str[left+1] == 0:
                left += 1
        else:
            left += 1
    return input_str

input_str = [1,0,2,3,0,4]
print(lateZero(input_str))
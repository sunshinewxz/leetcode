# solution 1: time complexity O(nlogn)
import bisect

def subarrayK(k, input_list):
    if len(input_list) == 0:
        return 0
    stack = [input_list[0]]
    for i in range(1, len(input_list)):
        if len(stack) < k:
            index = bisect.bisect_left(stack, input_list[i])
            stack = stack[:index] + [input_list[i]] + stack[index:]
            continue
        if stack[0] < 0 and input_list[i] > stack[0]:
            stack.pop(0)
            index = bisect.bisect_left(stack, input_list[i])
            stack = stack[:index] + [input_list[i]] + stack[index:]
        elif stack[0] > 0 and input_list[i] > 0:
            index = bisect.bisect_left(stack, input_list[i])
            stack = stack[:index] + [input_list[i]] + stack[index:]
    print(stack)
    return sum(stack)

# print(subarrayK(2, [1,1,1,1,1,1]))


# solution 2: O(n)
def subarrayK_sliding(k, input_list):
    if len(input_list) == 0:
        return 0
    max_sum = [0 for i in range(len(input_list))]
    max_sum[0] = input_list[0]
    for i in range(1, len(input_list)):
        max_sum[i] = max(input_list[i], input_list[i] + max_sum[i-1])
    window = 0
    for i in range(k):
        window += input_list[i]
    result = window
    for i in range(k, len(input_list)):
        window = window + input_list[i] - input_list[i-k]
        result = max(result, window, window+max_sum[i-k])
    return result
print(subarrayK_sliding(2, [-4, -2, 1, -3]))


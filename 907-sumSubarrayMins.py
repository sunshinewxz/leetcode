class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        if len(A) == 1:
            return A[0]
        for i in range(len(A)):
            if len(stack) == 0:
                stack.append(i)
                continue
            else:
                if A[i] >= A[stack[-1]]:
                    stack.append(i)
                else:
                    while(len(stack) > 0 and A[i] < A[stack[-1]]):
                        index = stack.pop()
                        temp = A[index]
                        if len(stack) > 0:
                            result += temp * ((i - stack[-1] -1) + (index-1-stack[-1])*(i-1-index))
                        else:
                            result += temp * (i+ index*(i-index-1))
                    stack.append(i)
        if len(stack) > 0:
            while(len(stack) > 0):
                index = stack.pop()
                temp = A[index]
                if len(stack) == 0:
                    result += temp * (len(A) + index*(len(A)-index-1))
                else:
                    result += temp * ((len(A) - stack[-1] - 1)+(index-1-stack[-1])*(len(A)-1-index))
        result = result%(10**9+7)
        return result
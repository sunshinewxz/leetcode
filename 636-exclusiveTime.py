import re
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # log_info = [[0,0] * n]
        result = [0 for i in range(n)]
        stack = []
        for i in range(len(logs)):
            if 'start' in logs[i]:
                id = int(re.findall(r'(\d*):start', logs[i])[0])
                start_time = int(re.findall(r'start:(\d*)', logs[i])[0])
                if len(stack) == 0:
                    stack.append([id, start_time])
                else:
                    pre_id = stack[-1][0]
                    result[pre_id] += (start_time - stack[-1][1])
                    stack.append([id, start_time])
            else:
                id = int(re.findall(r'(\d*):end', logs[i])[0])
                end_time = int(re.findall(r'end:(\d*)', logs[i])[0])
                print(end_time)
                thre = stack.pop()
                result[id] += (end_time - thre[1] + 1)
                if len(stack) > 0:
                    stack[-1][1] = end_time+1
        return result

# solution 2
import re
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # log_info = [[0,0] * n]
        result = [0 for i in range(n)]
        stack = []
        for log in logs:
            log = log.split(':')
            if log[1] == 'start':
                id = int(log[0])
                start_time = int(log[2])
                if len(stack) == 0:
                    stack.append([id, start_time])
                else:
                    pre_id = stack[-1][0]
                    result[pre_id] += (start_time - stack[-1][1])
                    stack.append([id, start_time])
            else:
                id = int(log[0])
                end_time = int(log[2])
                thre = stack.pop()
                result[id] += (end_time - thre[1] + 1)
                if len(stack) > 0:
                    stack[-1][1] = end_time+1
        return result
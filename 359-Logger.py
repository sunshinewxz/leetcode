class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.print_info = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.print_info:
            pre_time = self.print_info[message]
            if timestamp - pre_time >= 10:
                self.print_info[message] = timestamp
                return True
            else:
                return False
        else:
            self.print_info[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
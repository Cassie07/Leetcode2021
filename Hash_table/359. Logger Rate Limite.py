class Logger:

    def __init__(self):
        self.msg_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.msg_time:
            self.msg_time[message] = timestamp + 10
            return True
        else:
            if timestamp < self.msg_time[message]:
                return False
            else:
                self.msg_time[message] = timestamp + 10
                return True

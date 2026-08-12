class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.mini.append(value)
        else:
            self.mini.append(min(self.mini[-1] , value ))
            self.stack.append(value)

    def pop(self) -> None:
        if not self.stack :
            return 
        self.stack.pop() 
        self.mini.pop() 

    def top(self) -> int:
        if not self.stack :
            return 
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack :
            return 
        return self.mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

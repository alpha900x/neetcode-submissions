class MinStack:
    
    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.mval=0
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mval>=val:
            self.mval=val
            self.minstack.append(val)

    def pop(self) -> None:
        val=self.stack.pop()
        if len(self.minstack)!=0 and val==self.minstack[-1]:
            self.minstack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack)==0:
            return min(self.stack)
        else:
            return self.minstack[-1]

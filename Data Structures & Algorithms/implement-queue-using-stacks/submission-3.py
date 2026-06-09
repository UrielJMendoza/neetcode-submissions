class MyQueue:
    #so im thinking 
    #
    def __init__(self):


        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        #adds element to back of queue
       

        

    def pop(self) -> int:
        if not self.s2:
            for i in range(len(self.s1)):
            
                self.s2.append(self.s1.pop())
        
        first = self.s2.pop()

        return first


        

    def peek(self) -> int:
        if not self.s2:
            for i in range(len(self.s1)):
            
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
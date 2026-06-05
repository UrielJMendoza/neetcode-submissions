class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for i in range(len(tokens)):
        

            if tokens[i] == '+':
                if stack and len(stack) > 1:
                    numADD1 = int(stack.pop())
                    numADD2 = int(stack.pop())
                    stack.append(numADD1+numADD2)


            elif tokens[i] == '-':
                if stack and len(stack) > 1:
                    numADD3 = int(stack.pop())
                    numADD4 = int(stack.pop())
                    stack.append(numADD4-numADD3)



            elif tokens[i] == '*':
                if stack and len(stack) > 1: 
                    numADD5 = int(stack.pop())
                    numADD6 = int(stack.pop())
                    stack.append(numADD6*numADD5)


            elif tokens[i] == '/':
                if stack and len(stack) > 1:
                    numADD7 = int(stack.pop())
                    numADD8 = int(stack.pop())
                    stack.append(int(numADD8/numADD7))
            else:
                stack.append(int(tokens[i]))
        num = stack[0]
        return num

        
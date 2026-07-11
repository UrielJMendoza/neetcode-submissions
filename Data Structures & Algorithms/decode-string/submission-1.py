class Solution:
    #So I guess my first idea is to use a stack. 
    #Then my second idea is to go and pop the first character, check what the first character is, and pop it. 

    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subtr = ""
                while stack[-1]!= "[":
                    subtr = stack.pop() + subtr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * subtr)
        return "".join(stack)
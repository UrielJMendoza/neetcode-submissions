class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(',
        ']':'[',
        '}':'{'
        }
        for n in s:
            if n not in hashmap:
                stack.append(n)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[n]:
                        return False
        return not stack

                



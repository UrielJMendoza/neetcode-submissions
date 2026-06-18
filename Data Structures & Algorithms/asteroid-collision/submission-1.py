class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            #this is well the collision case
            while stack and a < 0 and stack[-1] > 0:
                #have a while statment for multiple collisions until no more
                #create a difference to calc what collsion wins
                diff = a + stack[-1]

                #since diff < 0 means 
                if diff < 0:
                    stack.pop()

            
                elif diff > 0:
                    a = 0 

                else:
                    stack.pop()
                    a = 0
            if a:
                stack.append(a)
        return stack


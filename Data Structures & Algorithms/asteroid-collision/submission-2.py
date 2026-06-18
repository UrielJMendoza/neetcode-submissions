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
                #index in list astroids + top stack is negative so -3 + 2 = -1 so pop 2
                if diff < 0:
                    stack.pop()

            
                elif diff > 0:
                    #index in list astroids + top stack is positive so -4 + 5 = 1 since the while loop
                    #checks if collsion if a is negative
                    #remove a make it not added
                    a = 0 

                else:
                    # else remove both
                    stack.pop()
                    a = 0
            if a:
                #if all test and collsions then append a into stack
                stack.append(a)

        #then outside of all a appened then all collsions then return stack
        return stack


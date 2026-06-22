class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # sort in ascending order burb

        light = 0 
        heavy = len(people) -1
        boats = 0 
        while light <= heavy:
            boats +=1
            remaining = limit - people[heavy]
            heavy -=1
            if light <= heavy and people[light] <= remaining:
                light +=1

        return boats
       
                

            
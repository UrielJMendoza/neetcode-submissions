

class TimeMap:

    def __init__(self):
        self.Hash = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        ## maybe doublde for loop
        ## go through all get/sets
        ## then based on get or set in second loop do specfic action to append to hash
        if key not in self.Hash:
            self.Hash[key] = []
        self.Hash[key].append([value, timestamp])
            



        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.Hash.get(key, [])
        
        low = 0
        high = len(values) - 1
        
        while low <= high:
            
            mid = (low + high) //2
            
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1

            else:
                high = mid - 1 
                
        return res
                


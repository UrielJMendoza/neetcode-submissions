# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

    
        #dummy = ListNode(0)
        #new = dummy
        
        givenlist = head

        
        Tracker = set()
        #while dummy.next
        #ad check if  its in if not add dummy.next loction reference and 
        #so im thinking of using a hashmap to count the next refernce or location it wants to go to 
        #if the location is in hashmap then return true
        ##out the loop return false no cycle
        while givenlist:
            if givenlist in Tracker:
                return True
            else:
                Tracker.add(givenlist)
            givenlist = givenlist.next
        
        return False




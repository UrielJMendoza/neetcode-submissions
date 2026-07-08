class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #im thinking  go through both linked list
        ## add then to a array
        ##
        ## then loop through arrays adding them up 
        #### theen loop through product creating the output linkedlist
        ##
        dummy = ListNode(0)
        current = dummy
        carry = 0
       
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            k = val1 + val2 + carry
            
            digit = k % 10             # ones-place digit goes in the node
            carry = k // 10

            newNode = ListNode(digit)
            current.next = newNode
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
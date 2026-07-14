class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the list first
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
            
        # If we remove the first node
        if length == n:
            return head.next
            
        # Navigate to the node right before the one to be removed
        target = length - n
        current = head
        counter = 1
        while counter < target:
            current = current.next
            counter += 1
            
        # Skip the nth node from the end
        current.next = current.next.next
        return head
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ##what im thinking is while both not null compare list1 and list2 
        ##make new linked list and awlays add the smallest 
        ##return list

        dummy = ListNode(0)
        new = dummy
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                new.next = curr2
                curr2 = curr2.next
            else:
                new.next = curr1
                curr1 = curr1.next
            new = new.next
          
        new.next = curr1 or curr2
            
        return dummy.next
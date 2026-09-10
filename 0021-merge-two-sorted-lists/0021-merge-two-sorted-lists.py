class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() #dummy=curr (curr maintains the merged list and dummy is at the head but first node is initialzed null and we dont want to include that in the ansver)
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1  #temp = list1        # 1. Save original list1 node
                                                #  list1 = list1.next  # 2. Advance list1 to the next node
                                                 # cur = temp          # 3. Move cur to the saved node
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
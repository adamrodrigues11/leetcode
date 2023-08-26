# Given two sorted lists of integers (non-decreasing order), merge them in order
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my initial solution (not realizing i could remove some cases using a dummy node)
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = None
        head = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    current = head
                else: 
                    current.next = list1
                    current = current.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    current = head
                else:
                    current.next = list2 
                    current = current.next
                list2 = list2.next
        while list1:
            if not head:
                head = list1
                current = head
            else:
                current.next = list1
                current = current.next
            list1 = list1.next
        while list2:
            if not head:
                head = list2
                current = head
            else:
                current.next = list2
                current = current.next
            list2 = list2.next
        return head
    
# improved solution using a dummy and better appending
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val: 
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2 
                list2 = list2.next
            current = current.next
        
        # append remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next
    

# Solution 2: Recursive solution
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
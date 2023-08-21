# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number = ""

        while head.next != None:
            number += str(head.val)
            head.next

        number = int(number)
        number = number * 2
        number = str(number)

        for i in number:
            head.val = int(i)
            head.next

        return head

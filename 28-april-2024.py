class Solution:
    def deleteMid(self,head):
        if not head.next:
            return None
        fast=head.next.next
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
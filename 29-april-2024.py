class Solution:
    def deleteK(self, head, k):
        if k==1:
            return None
        temp=head.next
        prev=head
        c=1
        while temp:
            c+=1
            if c%k==0:
                prev.next=temp.next
            prev=temp
            temp=temp.next
        return head
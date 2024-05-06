class Solution():
    def sortDoubly(self,head):
        tail = head
        while tail.next:
            tail=tail.next
        def merge(head,mid,tail):
            temp=[]
            i,j=head,mid.next
            while i!=mid.next and j!=tail.next:
                if i.data<j.data:
                    temp.append(i.data)
                    i = i.next
                else:
                    temp.append(j.data)
                    j=j.next
            if i!=mid.next:
                while i!=mid.next:
                    temp.append(i.data)
                    i = i.next
            if j!=tail.next:
                while j!=tail.next:
                    temp.append(j.data)
                    j=j.next
            k=head
            for i in temp:
                k.data=i
                k=k.next
        def mergesort(head,tail):
            if head!=tail:
                temp,mid=head,head
                while temp!=tail and temp.next!=tail:
                    temp=temp.next.next
                    mid=mid.next
                mergesort(head,mid)
                mergesort(mid.next,tail)
                merge(head,mid,tail)
        mergesort(head,tail)
        return head
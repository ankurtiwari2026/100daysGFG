
class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        vowels = ["a","e","i","o","u"]
        dummy = Node("p")
        dummy.next = head
        temp = dummy
        curr = dummy
        while temp and temp.next:
            if temp.next.data not in vowels:
                break
            temp = temp.next
            curr = curr.next
        while curr and curr.next:
            if curr.next.data in vowels:
                front = temp.next
                temp.next = curr.next
                temp = temp.next
                curr.next = temp.next
                temp.next = front
            else:
                curr = curr.next
        return dummy.next
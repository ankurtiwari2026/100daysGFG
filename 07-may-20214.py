from collections import deque
def reverseLevelOrder(root):
    ans=[]
    if root ==None:
        return
    q=deque()
    q.append(root)
    while q:
        n=len(q)
        for i in range(n):
            temp=q.popleft()
            ans.append(temp.data)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)
    ans.reverse()
    return ans
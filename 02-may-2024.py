

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        # arr = []
        res = []
        q = []
        q.append(root)
        while(q):
            temp = q.pop(0)
            res.append(temp)
            if(temp.data == -1):
                continue
            if(temp.left):
                q.append(temp.left)
            else:
                q.append(Node(-1))
            if(temp.right):
                q.append(temp.right)
            else:
                q.append(Node(-1))
        # for i in res:
        #     print(i.data)
        return res
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        if(len(a)==0):
            return None
        else:
            root = a[0]
            j = 0
            i = 1
            while(i<len(a)):
                if(a[j].data==-1):
                    j+=1
                    continue
                if(a[i].data!=-1):
                    a[j].left = a[i]
                else:
                    a[j].left = None
                i+=1
                if(a[i].data!=-1):
                    a[j].right = a[i]
                else:
                    a[j].right = None
                i+=1
                j+=1
            return root
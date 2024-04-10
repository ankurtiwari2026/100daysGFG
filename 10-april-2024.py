def findSingle(self, n, arr):
    
    ans=0
    for i in range(n):
        ans^=arr[i]
    return ans    
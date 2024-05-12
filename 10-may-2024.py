class Solution:
    
    def CombinationSum2(self, arr, n, k):
        arr.sort()
        res=[]
        def backtracking(start,subset,k): 
            if k==0:
                res.append(subset)
                return
            if k<0:
                return    
            for i in range(start,len(arr)):
                if i>start and arr[i]==arr[i-1]:
                    continue
                backtracking(i+1,(subset+[arr[i]]),k-arr[i])
        backtracking(0,[],k)
        return res                
        
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        set1=set(arr1)
        set2=set(arr2)
        union_list=set1 | set2
        union_list1=sorted(union_list)
        return union_list1
        print(union_list1)

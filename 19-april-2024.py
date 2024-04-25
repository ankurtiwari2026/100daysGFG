from collections import defaultdict
class Solution:
    def twoRepeated(self, arr , n):
        d = defaultdict(list)     
        for i in range(n+2):
            d[arr[i]].append(i)
        
        ans = [i for i in d if len(d[i])>1]
        
        if d[ans[0]][1]<d[ans[1]][1]:
            return ans
        else:
            return ans[::-1]


class Solution:
    def reversedBits(self, x):
        bit=31
        ans=0
        while x:
            if x%2:
                ans+=1<<bit
            bit-=1
            x//=2
        return ans    
        
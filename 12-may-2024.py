
class Solution:
    def minSteps(self, d):
        temp=0
        ans=0
        while temp<d:
            ans+=1
            temp+=ans
        if temp==d:
            return ans
        diff=temp-d
        if diff%2==0:
            return ans
        if ans%2==0:
            return ans+1
        else:
            return ans+2
     
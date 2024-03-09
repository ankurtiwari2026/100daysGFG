class Solution:
    def nthCharacter(self, s, r, n):
        
        for i in range(r):
            s1=''
            for j in range(n+1):
                if s[j]=="0":
                    s1=s1+"01"
                else:
                    s1=s1+"10"
            s=s1
        return s1[n]
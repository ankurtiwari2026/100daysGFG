class Solution:
	def removeDuplicates(self,str):
	    s=""
	    for i in str:
	        if i not in s:
    	        s+=i
    	return s     
	         
class Solution:
	def NBitBinary(self, n):
	    res=[]
	    def one(string,length,zeros):
	        if length==n:
	            res.append(string)
	            return 
	        one(string+'1',length+1,zeros)
	        if (length-zeros)>zeros:
	            one(string+'0',length+1,zeros+1)
	    one('1',1,0)
	    return res        
	            
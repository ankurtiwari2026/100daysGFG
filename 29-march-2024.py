class Solution:
	def isEularCircuitExist(self, v, adj):
	    
	    arr = [len(i) % 2 == 0 for i in adj]
        return all(arr)
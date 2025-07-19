class Solution:
	def maxProduct(self,arr):
	    n = len(arr)
	    left = 1
	    right = 1
	    maxp = arr[0]
	    for i in range(n):
    	    if left == 0:
    	        left = 1
    	    if right == 0:
    	        right = 1
    	       
    	    left *= arr[i]
    	    
    	    right *= arr[n-i-1]
    	    
    	    maxp = max(left,right,maxp)
        return maxp
	        
	    
	    
		  
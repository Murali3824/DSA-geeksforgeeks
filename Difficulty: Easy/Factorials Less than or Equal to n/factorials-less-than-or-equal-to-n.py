#User function Template for python3

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
class Solution:
    def factorialNumbers(self, n):
    	l=[]
    	for i in range(1,n+1):
    	    a=fact(i)
    	    if a<=n:
    	        l.append(a)
    	    else:
    	        break
    	return l 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
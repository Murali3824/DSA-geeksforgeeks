#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        if n==0:
            return 0
        return n**3 + self.sumOfSeries(n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends
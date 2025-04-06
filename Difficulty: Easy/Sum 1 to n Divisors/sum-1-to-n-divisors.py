#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
    	sum = 0
    	if 1 <= n <= 10**5:
            for i in range(1, n + 1):
                sum += i * (n // i)
        return sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends
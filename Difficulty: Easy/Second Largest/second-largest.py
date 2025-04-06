#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        l1 = arr[0]
        l2 = -1
        for i in range(0,len(arr)):
            if l1<arr[i]:
                l1=arr[i]
        for i in range(0,len(arr)):
            if(l2<arr[i] and arr[i]!=l1):
                l2=arr[i]
        return l2
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
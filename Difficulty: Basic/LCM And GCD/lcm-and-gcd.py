#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends

class Solution:
    def lcmAndGcd(self, a, b):
        # Find GCD using Euclidean algorithm
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        l = (a * b) // g
        return [l, g]



#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends
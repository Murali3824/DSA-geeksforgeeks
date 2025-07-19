#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        arr.sort()
        n = len(arr)
        return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])
                    
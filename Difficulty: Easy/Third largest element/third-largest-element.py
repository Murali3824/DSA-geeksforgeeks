class Solution:
    def thirdLargest(self,arr):
        n = len(arr)
        arr.sort()
        return arr[n-3]
class Solution:
    def maxSubarraySum(self, arr):
        res = arr[0]
        maxend = arr[0]
        for i in range(1,len(arr)):
            maxend = max(maxend + arr[i],arr[i])
            res = max(res,maxend)
        return res
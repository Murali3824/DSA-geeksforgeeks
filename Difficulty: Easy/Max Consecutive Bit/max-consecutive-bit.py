class Solution:
    def maxConsecBits(self, arr):
        n =len(arr)
        maxcount,count = 0,1
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                count += 1
            else:
                maxcount = max(count,maxcount)
                count = 1
        return max(maxcount,count)
        
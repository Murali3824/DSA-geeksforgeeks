class Solution:
    def firstRepeated(self,arr):
        n = len(arr)
        freq = {}
        
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        for i in range(n):
            if freq[arr[i]] > 1:
                return i+1
        return -1
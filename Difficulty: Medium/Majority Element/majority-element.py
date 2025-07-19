class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        freq = defaultdict(int)
        
        for num in arr:
            freq[num] += 1
            
            if freq[num] > n / 2:
                return num
        return -1
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        missing = repeated = -1
        freq = [0]*(n+1)
        for num in arr:
            freq[num] += 1
        
        for i in range(n+1):
            if freq[i] == 0:
                missing = i
            elif freq[i] == 2:
                repeated = i
        return [repeated,missing]
                
            


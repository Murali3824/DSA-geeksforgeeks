class Solution:
    def longestKSubstr(self, s, k):
        left = maxlen = 0
        freq = {}
        
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
                
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            if len(freq) == k:
                maxlen = max(maxlen,right-left+1)
            
        return maxlen if maxlen != 0 else -1    
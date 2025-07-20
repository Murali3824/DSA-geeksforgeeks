class Solution:
    def areAnagrams(self, s1, s2):
        freq = {}
       
        for num in s1:
            if num not in freq:
               freq[num] = 1
            else:
                freq[num]+=1
                
        for char in s2:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] < 0:
                return False
        return True
            
            
             
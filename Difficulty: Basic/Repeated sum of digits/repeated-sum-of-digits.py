#User function Template for python3
class Solution:
    def repeatedSumOfDigits (self,N):
        while N >= 10:
            sums = 0
            while N > 0:
                sums += N%10
                N = N // 10
            N = sums
        return sums
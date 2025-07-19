class Solution:
    def rearrange(self, arr):
        n = len(arr)
        pos = []
        neg = []
        
        for i in range(n):
            if arr[i] >= 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        i = j = k = 0
        turn = 0

        while i < len(pos) and j < len(neg):
            if turn == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
            turn = 1 - turn

        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1

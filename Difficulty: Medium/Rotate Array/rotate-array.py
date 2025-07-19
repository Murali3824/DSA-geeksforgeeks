class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  
        temp = []

        for i in range(d):
            temp.append(arr[i])

        for i in range(d, n):
            arr[i - d] = arr[i]

        j = 0
        for i in range(n - d, n):
            arr[i] = temp[j]
            j += 1
        
        return arr

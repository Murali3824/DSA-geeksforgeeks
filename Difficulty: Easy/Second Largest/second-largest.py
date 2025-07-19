class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        secondlargest = -1
        for i in range(len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        for i in range(len(arr)):
            if arr[i]>secondlargest and arr[i] != largest:
                secondlargest = arr[i]
        return secondlargest
class Solution:
    def findKRotation(self, arr):
        left, right = 0, len(arr)-1
        min_val = float('inf')
        index = -1
          
        while left <= right:
            mid = (left + right) // 2
            
            if arr[left] <= arr[mid]:
              if min_val > arr[left]:
                min_val = arr[left]
                index = left
              left = mid + 1
              
            else:
              if min_val > arr[mid]:
                min_val = arr[mid]
                index = mid
              right = mid - 1
              
        return index
        
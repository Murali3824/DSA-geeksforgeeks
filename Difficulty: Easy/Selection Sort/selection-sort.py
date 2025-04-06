#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(0,n-1):
            min = i
            for j in range(i+1,n):
                if (arr[j]<arr[min]):
                    min = j
            temp = arr[min]
            arr[min] = arr[i]
            arr[i] = temp
        return arr


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")

# } Driver Code Ends
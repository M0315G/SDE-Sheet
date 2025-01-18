# Question:
# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

# Logic:
# Binary search.

class Solution:
    ##Complete this function
    def binarySearch(self, arr, low, high, k):
        if low>high:
            return False
        
        mid = (low+high)//2
        if k == arr[mid]:
            return True
        elif k < arr[mid]:
            return self.binarySearch(arr, low, mid-1, k)
        else:
            return self.binarySearch(arr, mid+1, high, k)
    
    def searchInSorted(self,arr, k):
        #Your code here
        return self.binarySearch(arr, 0, len(arr)-1, k)
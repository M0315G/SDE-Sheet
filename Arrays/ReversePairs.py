# Question:
# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
# --> 0 <= i < j < nums.length and
# --> nums[i] > 2 * nums[j].

# Logic:
# --> Brute force is to do an O(n^2) approach where we compare each element to the other element.
# --> Optimised approch is to do this during merge sort
#   --> Look at the problem "CountInversion.py" to understand the initial intuition, then building up on it:
#       Here we want to see that we get such [i, j] that arr[i] > 2*arr[j]
#       Ah, too much to write --> look at YT for this :)

class Solution:
    def merge(self, low, mid, high, arr):
        ans = []
        left, right = low, mid+1
        count = 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                ans.append(arr[left])
                left += 1
            else:
                if arr[left] > 2*arr[right]:
                    count += (mid - left + 1)
                ans.append(arr[right])
                right += 1

        while left <= mid:
            ans.append(arr[left])
            left += 1
        
        while right <= high:
            ans.append(arr[right])
            right += 1
        
        for i in range(low, high+1):
            arr[i] = ans[i - low]

        return count

    def countPairs(self, low, mid, high, arr):
        count = 0
        right = mid + 1
        for i in range(low, mid+1):
            while right <= high and arr[i] > 2*arr[right]:
                right += 1
            count += (right - (mid + 1))
        return count


    def mergeSort(self, low, high, arr):
        cnt = 0
        if low >= high:
            return cnt
        mid = int((low + high)/2)
        cnt += self.mergeSort(low, mid, arr)
        cnt += self.mergeSort(mid+1, high, arr)
        cnt += self.countPairs(low, mid, high, arr)
        self.merge(low, mid, high, arr)
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(0, len(nums)-1, nums)
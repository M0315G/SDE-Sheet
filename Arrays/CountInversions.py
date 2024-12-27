# Question:
# For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
# An inversion is defined for a pair of integers in the array/list when the following two conditions are met.
# A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

# 1. 'ARR[i] > 'ARR[j]' 
# 2. 'i' < 'j'

# Where 'i' and 'j' denote the indices ranging from [0, 'N').

# Logic:
# --> Brute force is to do an O(n^2) approach where we compare each element to the other element.
# --> Optimised approach is to use merge sort and when we're merging we introduce a counter which tells us if the left is greater than right
#       --> And since the arrays we compare in merge sort are sorted, we can say that if left > right; all elements from left to mid will be greater than right thus we increment count by (mid - left + 1)


def merge(low, mid, high, arr):
    ans = []
    left, right = low, mid+1
    count = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            ans.append(arr[left])
            left += 1
        else:
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


def mergeSort(low, high, arr):
    cnt = 0
    if low >= high:
        return cnt
    mid = int((low + high)/2)
    cnt += mergeSort(low, mid, arr)
    cnt += mergeSort(mid+1, high, arr)
    cnt += merge(low, mid, high, arr)
    return cnt

def getInversions(arr, n):
    return mergeSort(0, n-1, arr)



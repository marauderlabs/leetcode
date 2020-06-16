# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34-find-first-and-last-position-of-element-in-sorted-array.py


class Solution:
# A simple linear solution
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         low = high = -1;
#         for i, n in enumerate(nums):
#             if n == target:
#                 if low == -1:
#                     low = i
#                 high = i
#
#             if n > target: # why search unnecessarily?
#                 break
#
#         return [low, high]

# The proper binary solution
    def binSearch(self, arr, target, go_right=True):
        index, low, high = -1, 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] < target:
                low = mid+1
            elif arr[mid] > target:
                high = mid-1
            else:
                index = mid
                if go_right:
                    low = mid+1
                else:
                    high = mid-1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = high = -1
        l = 0
        h = len(nums)-1
        low = self.binSearch(nums, target, go_right=False)
        high = self.binSearch(nums, target, go_right=True)

        return [low, high]

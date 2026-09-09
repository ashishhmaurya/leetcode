class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid +1
                else:
                    right = mid -1
            return left
        return binary_search(nums,target)                
        
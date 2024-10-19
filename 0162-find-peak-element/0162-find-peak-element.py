class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        left_pointer = 1
        right_pointer = len(nums) - 2

        while left_pointer <= right_pointer:
            mid_point = left_pointer + (right_pointer - left_pointer)//2
            if (mid_point == 0 or nums[mid_point-1] <= nums[mid_point]) and (mid_point == len(nums)-1 or nums[mid_point+1] <= nums[mid_point]):
                return mid_point
            if mid_point == 0 or nums[mid_point-1] < nums[mid_point]:
                left_pointer = mid_point + 1
            else:
                right_pointer = mid_point - 1
        return -1
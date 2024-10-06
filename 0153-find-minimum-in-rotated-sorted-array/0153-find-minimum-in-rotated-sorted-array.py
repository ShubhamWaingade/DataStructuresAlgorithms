class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            mid_point = left_pointer + (right_pointer - left_pointer) // 2
            if  nums[mid_point] > nums[right_pointer]:
                left_pointer = mid_point + 1
            else:
                right_pointer = mid_point
        return nums[left_pointer]
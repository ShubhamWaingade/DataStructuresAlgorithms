class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for ind in range(len(nums)-1, -1, -1):
            if ind == 0:
                nums.sort()
                return
            elif nums[ind-1] < nums[ind]:
                pivot_index = ind - 1
                pivot_element = nums[ind - 1]
                break
        
        for index in range(len(nums)-1, -1, -1):
            if nums[index] > pivot_element:
                nums[index], nums[pivot_index] = nums[pivot_index], nums[index]
                break
        
        left_pointer = pivot_index + 1
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer -= 1
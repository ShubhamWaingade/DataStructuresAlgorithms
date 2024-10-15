class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1
        for ind in range(1, len(nums)):
            if nums[ind-1] != nums[ind]:
                nums[insert_index] = nums[ind]
                insert_index += 1
        return insert_index
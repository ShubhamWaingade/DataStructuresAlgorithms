class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = nums
        sorted_nums.sort()
        final_sum = 0

        n = len(nums)
        i = 0
        while i < n -1:
            final_sum += min(sorted_nums[i], sorted_nums[i+1])
            i += 2
        return final_sum

        
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        ans = nums[0]

        for i in range(0,len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            if sum > ans:
                ans = sum
        return ans
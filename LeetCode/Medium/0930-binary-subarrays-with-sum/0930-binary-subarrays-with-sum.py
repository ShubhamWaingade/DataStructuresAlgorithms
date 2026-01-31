class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        temp_hash = {0:1}
        # prefix_sum[0] = nums[0]
        subarray_count = 0
        n = len(nums)

        for i in range(n):
            prefix_sum += nums[i]
            # if prefix_sum == goal:
            #     subarray_count += 1
            subarray_count += temp_hash.get(prefix_sum - goal, 0)
            temp_hash[prefix_sum] = temp_hash.get(prefix_sum, 0) + 1
        return subarray_count


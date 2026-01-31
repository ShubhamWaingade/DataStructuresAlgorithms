class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # count = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         current_sum = 0
        #         for m in range(i, j+1):
        #             current_sum += nums[m]
        #         if current_sum == k:
        #             count += 1
        # return count

        prefix_sum = 0
        sub_array_count = 0
        temp_hashmap = {}

        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == k:
                sub_array_count += 1
            sub_array_count += temp_hashmap.get(prefix_sum-k, 0)
            temp_hashmap[prefix_sum] = temp_hashmap.get(prefix_sum, 0) + 1
        return sub_array_count
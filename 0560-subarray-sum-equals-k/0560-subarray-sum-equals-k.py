class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        array_len = len(nums)
        temp_hashmap = {}
        prefix_sum_nums = 0
        sub_array_count = 0
        
        for index in range(array_len):
            prefix_sum_nums += nums[index]
            if prefix_sum_nums == k:
                sub_array_count += 1
            sub_array_count += temp_hashmap.get(prefix_sum_nums-k, 0)
            temp_hashmap[prefix_sum_nums] = temp_hashmap.get(prefix_sum_nums, 0) + 1
        
        return sub_array_count
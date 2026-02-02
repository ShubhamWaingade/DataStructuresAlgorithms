class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        given_sum_k = 0
        prefix_sum = 0
        temp_hash = {}

        new_nums = [-1 if i == 0 else i for i in nums]

        for i in range(len(new_nums)):
            prefix_sum += new_nums[i]
            if prefix_sum == given_sum_k:
                max_len = i + 1
            
            elif prefix_sum in temp_hash:
                new_temp_len = i - temp_hash.get(prefix_sum)
                max_len = max(max_len, new_temp_len)
            else:
                temp_hash[prefix_sum] = i
        return max_len

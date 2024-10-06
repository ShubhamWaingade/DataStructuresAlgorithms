class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        max_sub_array_product = nums[0]
        min_sub_array_product = nums[0]

        for indx in range(1, len(nums)):
            current_min = min_sub_array_product * nums[indx]
            current_max = max_sub_array_product * nums[indx]

            max_sub_array_product = max(current_max, current_min, nums[indx])
            min_sub_array_product = min(current_max, current_min, nums[indx])

            max_product = max(max_product , max_sub_array_product, min_sub_array_product, nums[indx])

        return max_product
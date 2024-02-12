class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_len = len(nums)
        prefix_nums = [0] * arr_len
        prefix_nums[0] = nums[0]
        
        pivot_index = -1
        
        for index in range(1, arr_len):
            prefix_nums[index] = prefix_nums[index-1] + nums[index]
        
        for index in range(arr_len):
            if index == 0:
                if prefix_nums[arr_len-1] - prefix_nums[index] == 0:
                    return index
            elif index == arr_len - 1:
                if prefix_nums[arr_len - 2] == 0:
                    return index
            else:
                if prefix_nums[index-1] == prefix_nums[arr_len-1] - prefix_nums[index]:
                    return index
        return -1

        
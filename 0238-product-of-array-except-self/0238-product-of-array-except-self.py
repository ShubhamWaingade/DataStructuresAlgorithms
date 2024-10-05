class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_len = len(nums)
        ans_arr = [0] * array_len
        prefix_product = [1] * array_len
        prefix_product[0] = nums[0]

        postfix_product = [1] * array_len
        postfix_product[-1] = nums[-1]

        for ind in range(array_len):
            if ind == 0:
                prefix_product[ind] = 1
            else:
                prefix_product[ind] = prefix_product[ind-1] * nums[ind-1]

        for ind in range(array_len-1, -1, -1):
            if ind == array_len - 1:
                postfix_product[ind] = 1
            else:
                postfix_product[ind] = postfix_product[ind+1] * nums[ind+1]

        for final_ind in range(array_len):
            ans_arr[final_ind] = prefix_product[final_ind] * postfix_product[final_ind]
        
        return ans_arr
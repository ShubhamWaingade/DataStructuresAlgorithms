class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)
        red_rgn = 0
        white_rgn = 0
        blue_rgn = 0
        
        while blue_rgn < arr_len:
            if nums[blue_rgn] == 2:
                blue_rgn += 1
            elif nums[blue_rgn] == 1:
                nums[white_rgn], nums[blue_rgn] = nums[blue_rgn], nums[white_rgn]
                white_rgn += 1
                blue_rgn += 1
            else:
                nums[red_rgn], nums[blue_rgn] = nums[blue_rgn], nums[red_rgn]
                red_rgn += 1
                if nums[blue_rgn] == 1:
                    nums[white_rgn], nums[blue_rgn] = nums[blue_rgn], nums[white_rgn]
                white_rgn += 1
                blue_rgn += 1
                
        
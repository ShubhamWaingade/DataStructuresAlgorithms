class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_index = {}
        
        for ind in range(len(nums)):
            if map_index.get(target-nums[ind], -1) != -1:
                return [ind, map_index[target-nums[ind]]]
                
            else:
                map_index[nums[ind]] = map_index.get(nums[ind], ind)
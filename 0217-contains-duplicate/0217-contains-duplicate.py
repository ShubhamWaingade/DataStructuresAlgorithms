class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record_map = {}
        status = False
        for ind in range(len(nums)):
            status = record_map.get(nums[ind], False)
            if status != False:
                return True
            record_map[nums[ind]] = record_map.get(nums[ind], True)
        return status
class Solution:
    def findBound(self, nums: List[int], target: int, is_first: bool) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid_point = left_pointer + (right_pointer - left_pointer) // 2
            if nums[mid_point] == target:
                if is_first:
                    if mid_point == left_pointer or nums[mid_point - 1] != target:
                        return mid_point
                    right_pointer = mid_point - 1
                else:
                    if mid_point == right_pointer or nums[mid_point + 1] != target:
                        return mid_point
                    left_pointer = mid_point + 1
            elif nums[mid_point] > target:
                right_pointer = mid_point - 1
            else:
                left_pointer = mid_point + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_position = [-1, -1]
        first_position = self.findBound(nums, target, True)
        if first_position == -1:
            return target_position
        second_position = self.findBound(nums, target, False)

        return [first_position, second_position]
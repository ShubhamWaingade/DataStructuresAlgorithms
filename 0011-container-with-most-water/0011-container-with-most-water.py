class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1

        max_volume = 0

        while left_pointer < right_pointer:
            current_volume = min(height[left_pointer], height[right_pointer]) * (
                right_pointer - left_pointer
            )
            max_volume = max(max_volume, current_volume)

            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_volume

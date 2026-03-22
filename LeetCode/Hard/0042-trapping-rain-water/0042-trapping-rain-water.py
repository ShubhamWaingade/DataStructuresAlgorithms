class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pref_max = [0] * n
        suf_max = [0] * n
        total_water_trapped = 0

        pref_max[0], suf_max[n-1] = height[0], height[n-1]

        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], height[i])

        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        for i in range(1, n-1):
            current_trapped_water = min(suf_max[i], pref_max[i]) - height[i]
            total_water_trapped += current_trapped_water
        
        return total_water_trapped
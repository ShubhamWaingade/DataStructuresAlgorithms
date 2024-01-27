class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for bit_index in range(32):
            if n & (1 << bit_index) > 0:
                ans |= 1 << (32 - bit_index - 1)
        return ans
        
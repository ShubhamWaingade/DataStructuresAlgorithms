class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        111 00
        How to know to shrink window or increase?
        Have to split, thus recursive and worse than O(n^2)

        Not every result starts at the beginning e.g. 111 00

        Is it possible to know exactly where the first 1 was, and then virify after
        count[1] == count[0]?

        Map each index to pait (count[0], count[1])
        Use the diff between the counts to lookup what we need
        """
        ans = 0
        diff_index = {}
        zero, one = 0, 0

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one - zero not in diff_index:
                diff_index[one - zero] = i
            
            if one == zero:
                ans = one + zero
            else:
                idx = diff_index[one - zero]
                ans = max(ans, i - idx)
        
        return ans
            

        


        
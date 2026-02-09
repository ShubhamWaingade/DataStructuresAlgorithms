class Solution:
    def expand(self, s, c1, c2, n):
        while c1 >= 0 and c2 < n and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return c1 + 1, c2

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_str = ""
        for i in range(n):
            c1, c2 = self.expand(s, i, i, n)
            temp_str = s[c1:c2]
            if len(ans_str) < len(temp_str):
                ans_str = temp_str
        
        for i in range(n-1):
            c1, c2 = self.expand(s, i, i+1, n)
            temp_str = s[c1:c2]
            if len(ans_str) < len(temp_str):
                ans_str = temp_str
        
        return ans_str
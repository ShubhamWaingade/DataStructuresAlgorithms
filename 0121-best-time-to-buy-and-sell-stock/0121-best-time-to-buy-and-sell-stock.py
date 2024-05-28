class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)
        suffix_max_arr = [0] * len(prices)
        suffix_max_arr[-1] = prices[-1]
        
        for ind in range(arr_len-2, -1, -1):
            suffix_max_arr[ind] = max(prices[ind], suffix_max_arr[ind+1])
        
        max_profit = 0
        
        for ind in range(arr_len-1):
            max_profit = max(max_profit, suffix_max_arr[ind+1]-prices[ind])
        return max_profit
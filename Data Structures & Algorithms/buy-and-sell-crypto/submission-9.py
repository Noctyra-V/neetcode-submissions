class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m = 0
        while j < len(prices):
            if prices[j] - prices[i]  >= 0:
                m = max(m,prices[j] - prices[i])
            else:
                i = j
            j += 1
        return m
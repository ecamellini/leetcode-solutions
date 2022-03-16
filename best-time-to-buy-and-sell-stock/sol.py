from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for buyDay, buyPrice in enumerate(prices):
            for sellPrice in prices[buyDay:]:
                profit = sellPrice - buyPrice
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit


solution = Solution()

assert solution.maxProfit([4, 6, 2, 5]) == 3
assert solution.maxProfit([7, 3, 8, 2, 1, 0, 0, 2, 3]) == 5
assert solution.maxProfit([4, 3, 1, 0]) == 0
assert solution.maxProfit([]) == 0
assert solution.maxProfit([1]) == 0
print("All tests passed.")

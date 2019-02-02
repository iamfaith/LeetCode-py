

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, minP = 0, None
        for p in prices:
            if minP is None or p < minP:
                minP = p

            if p - minP > maxProfit:
                maxProfit = p - minP

        return maxProfit


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])

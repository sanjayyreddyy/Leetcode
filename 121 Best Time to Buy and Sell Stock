# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if prices == sorted(prices)[::-1]:
        #     return 0
        # m= 0
        # for i in range(len(prices)-1):
        #     for j in range(i,len(prices)):
        #         m=max(m, prices[j]-prices[i])
        # return m


        buy = prices[0]
        m = 0
        for i in prices[1:]:
            if i<buy:
                buy = i
            m=max(m, i-buy)
        return m
            

        
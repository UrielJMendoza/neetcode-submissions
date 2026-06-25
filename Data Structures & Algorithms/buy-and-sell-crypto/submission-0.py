class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #so i know its a sliding window problem right 
        #so i need Left and right side of window
        #probabaly need a max proft variable

        maxProfit = []

        left = 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit.append(profit)
                ##move window over 
            elif prices[left] >= prices[right]:
                left = right
                right = left + 1


        
# so right pointer is i and increments making window grow
#left pointer slides right and kinda shrinks window based on some condtions
## we need to find one day to buy and a diferent day in the future to sell it 
## if no left pointer smaller than any oother thing in list return 0 profit 

#im thinking use left pointer and if left pointer greater than right pointer then move left bu
#calc left minus right for max profit comapre
        if not maxProfit:
            return 0


        return max(maxProfit)
            

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # check if the prices is empty or in proper formate
        if not prices:
            0
        
        profit = 0
        
        # for loop looking for the cheapest day
        for buy_price in range(len(prices)):
            # print("DEBUG:buy_price",buy_price)
            # print("DEBUG:sell_price",sell_price)
            # if prices[price_ind] < buy_price:
            #     buy_price = prices[price_ind]
            #     buy_ind = price_ind
            #     sell_price = prices[price_ind]
            # if (price_ind > buy_ind) and prices[price_ind] > sell_price:
            #     sell_price = prices[price_ind]
            for sell_price in range(buy_price,len(prices)):
                if prices[sell_price] - prices[buy_price] > profit:
                    profit = prices[sell_price] - prices[buy_price]

        
        return profit


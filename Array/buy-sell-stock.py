#Question:Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Approach:The code uses a simple approach to find the maximum profit from buying and selling a stock. 
# It iterates through the list of stock prices, updating the minimum price seen so far and calculating the maximum profit based on the price difference. 
# The final result is the maximum profit obtained.

# Time complexity: O(N)
# Space complexity: O(1)

#Question:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150


def buy_sell(prices):
    min_price,max_profit=float('inf'),0

    for price in prices:
        if price<min_price:
            min_price=price
        
        elif price-min_price>max_profit:
            max_profit=price-min_price
        
    return max_profit

prices=[7,1,5,3,6,4]
print(buy_sell(prices))
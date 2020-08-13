# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you 
# like (i.e., buy one and sell one share of the stock multiple times).

# You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

# Notes: 
# This is a "max-interval" or "max-difference" problem.  My initial thought is to try 2 pointers again, 
# where for each value the other pointer scans through and finds the max difference.  Need to develop a solution.
from typing import List
def maxProfit(self, prices: List[int]) -> int:
    # my initial thought is to use a 2 pointer approach, because this is effectively a             
    # "find the max difference problem".
    minp = 1000000 #or INT.max
    maxp = 0
    for i in range(0,len(prices)):
        # if the current price is less than the all time low, set it to the all-time low
        if(prices[i] < minp):
            minp = prices[i]
        # if the current price - all time low is greater than the best profit, set the new best profit
        elif(prices[i] - minp > maxp):
            maxp = prices[i]-minp

    # return the best profit
    return maxp

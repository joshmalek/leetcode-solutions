# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you 
# like (i.e., buy one and sell one share of the stock multiple times).

# You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

# Notes: 
# This is a "max-interval" or "max-difference" problem.  My initial thought is to try 2 pointers again, 
# where for each value the other pointer scans through and finds the max difference.
from typing import List
def maxProfit(self, prices: List[int]) -> int:
    
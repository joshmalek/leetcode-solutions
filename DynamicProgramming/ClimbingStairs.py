# Link: https://leetcode.com/problems/climbing-stairs/

# Notes: A basic backtracking algorithm.  We try and find the answers for all the subproblems before the main problem, and recursively work our way down.
# We cache our subproblems to save compute time through the recursion.

def helper(self,i,n,cache)-> int:
    if(i > n):
        return 0
    if(i == n):
        return 1
    if(i in cache):
        return cache[i]
    cache[i] = self.helper(i+1,n,cache)+self.helper(i+2,n,cache)
    return cache[i]

cache = {}
return(self.helper(0,n,cache))

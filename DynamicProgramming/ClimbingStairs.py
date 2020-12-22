# Link: https://leetcode.com/problems/climbing-stairs/

# Notes: Actual dynamic programming here.  Very simple and efficient. Stores the results of the runs before it.
def climbStairs(self, n: int) -> int:
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        dp = [0,1,2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]



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

#Link: https://leetcode.com/problems/first-bad-version/

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    
    while(left<right):
        mid = (right-left)//2 + left
        res = isBadVersion(mid)
        if(res == False):
            left = mid + 1
        else:
            right = mid
    return left
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

# Notes:
# A palindrome is a word or statment that reads the same backwards as forward.  So, my idea is to first strip the
# whitespace, then split into two based on length.  Then, reverse the second half and compare it to the first.  if
# they are equal, then return true.  I think this would be O(n), with O(n) space.

# Another way of doing this is a 2 pointer style, one pointing to the first and the other to the last.  Then,
# iterate through the string and compare that they are equal.  This is also O(n), but with O(1) space.

def isPalindrome(s: str) -> bool:
    e = []
    for i in s:
        if(i.isalnum()):
            e.append(i.lower())
    s = "".join(e)
    spl = len(s)//2
    if(len(s)%2):
        a = s[:spl]
        b = s[spl+1:]
    else:
        a = s[:spl]
        b = s[spl:]
    return a == b[::-1]

print(isPalindrome("race a car"))
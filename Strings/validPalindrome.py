# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

# Notes:
# A palindrome is a word or statment that reads the same backwards as forward.  So, my idea is to first strip the
# whitespace, then split into two based on length.  Then, reverse the second half and compare it to the first.  if
# they are equal, then return true.  I think this would be O(n).

def isPalindrome(self, s: str) -> bool:
    
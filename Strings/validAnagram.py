# Given two strings s and t , write a function to determine if t is an anagram of s.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

# Notes:
# Given that ASCII chars have a specific value to them, it would make sense that 2 strings would be anagrams if 
# they have the same total sum of character values and the same length.  This is O(n) as it passes through the strings
# once.  This O(1) space as only ints are used.  This won't actually work though as its possible to fool this.  ac
# will show up as equal to bb, as they have the same sum value.

# A valid solution would be to sort both strings, and then compare them.  Sorting would be O(nlogn), and iteration
# would be O(n), so the total time would be O(nlogn).

def isAnagram(s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False
    s = list(s)
    s = sorted(s)
    t = list(t)
    t = sorted(t)
    for i in range(0,len(s)):
        if(s[i]!=t[i]):
            return False
    return True
    


    # Try 1: doesn't work
    # sum_s = 0
    # sum_t = 0

    # for i in range(0,len(s)):
    #     sum_s += ord(s[i])
    #     sum_t += ord(t[i])

    # return(sum_s == sum_t)

print(isAnagram("ac","ca"))
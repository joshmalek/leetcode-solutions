# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

# Notes:
# My first immediate thought is to pass through the string, with a dictionary tracking how many appearances for each char.
# Then pass through the dictionary again, looking for any 1 appearances.  This would be O(n) runtime, and O(n) space.

def firstUniqChar(s: str) -> int:
    d = dict()
    for i,char in enumerate(s):
        if(char in d):
            d[char].append(i)
        else:
            d[char] = list()
            d[char].append(i)
    for i,char in enumerate(s):
        if(len(d[char]) == 1):
            return i
    return -1


print(firstUniqChar("loveleetcode"))
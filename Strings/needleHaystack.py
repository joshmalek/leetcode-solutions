# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

# Notes: 
# I feel this could be like a path finding problem, but that's overcomplicating.  My initital idea is to send a 
# pointer out looking for the first occurence of the first char in the needle string.  It will then iterate
# from there, and if it finds the full needle string there, it will return the index of the occurence.  This
# is inefficient, with it mostly likely being an O(n^2) solution.

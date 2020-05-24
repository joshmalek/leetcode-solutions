# Implement atoi which converts a string to an integer.  
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits 
# as possible, and interprets them as a numerical value.  
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have 
# no effect on the behavior of this function. If the first sequence of non-whitespace characters in str is not a valid 
# integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, 
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

# Notes:
# lstrip() all the white space from the left side, which leaves the number. Then look for a plus or minus if it exists.
# After that, iterate through the string and split out where the number stops.  Then, convert this number using int.  If
# this number is larger than INT MAX, return INT MAX (2^31).  This is O(n) runtime.
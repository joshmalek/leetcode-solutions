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

def myAtoi(str: str) -> int:
    s = str.strip()
    if(len(s) == 0):
        return 0
    s_index = 0
    sign = 1

    if(s[0] == '-'):
        sign = -1
        s_index = 1
    elif(s[0] == '+'):
        sign = 1
        s_index = 1
    elif(s[0].isdigit() == False):
        return 0
    i = s_index
    while(i < len(s) and s[i].isdigit()):
        i+=1
    if(s_index == i):
        return 0
    num = sign * int(s[s_index:i])
    if(num < pow(-2,31)):
        return(pow(-2,31))
    elif(num > pow(2,31)-1):
        return(pow(2,31)-1)
    else:
        return num

print(myAtoi("+"))

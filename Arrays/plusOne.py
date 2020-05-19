# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each 
# element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# Input: [1,2,3]
# Output: [1,2,4]

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

# Notes:
# First idea: start from the last index, and multiply each index working back by 10^index. The first
# spot will be 10^0 which is 1, second is 10, third is 100 and so on.  Add everything together,
# and add 1.  Convert the int to string, and split. Added the int version of split string to 
# return array. This would have runtime O(n) and O(n) space.

from typing import List
def plusOne(digits: List[int]) -> List[int]:
    i = len(digits)-1
    x = 0
    total = 0
    while(i >= 0):
        total += pow(10,x) * digits[i]
        i -= 1
        x += 1
    total += 1
    #convert total to string to allow it to be split 
    strtotal = str(total)
    i = 0
    ret = []
    while(i < len(strtotal)):
        ret.append(int(strtotal[i]))
        i+=1
    return ret

print(plusOne([0]))
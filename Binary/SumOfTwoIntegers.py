# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# Link: https://leetcode.com/problems/sum-of-two-integers/

# My first thought is to break each integer into bits, and then use bitwise operators to add them together.  I believe bitwise
# XOR and bitwise AND can help with this.
def getSum(self, a: int, b: int) -> int:

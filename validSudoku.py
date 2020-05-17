# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.   

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

# Notes: 
# First idea: brute force by checking every row for no duplicates, and then checking every
# column for no duplicates, and then checking every sub-box for no duplicates.  I think
# this would be O(n) but it would take a lot of space.


def isValidSudoku(board: List[List[str]]) -> bool:
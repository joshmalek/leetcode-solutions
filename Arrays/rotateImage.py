# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 
# 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

# Notes:
# My idea: First column becomes top row, 2nd column becomes middle row and so on.  To do this in place,
# it would require overwriting and tracking of each row.  So [2][0],[1][0],[0][0] becomes
# [0][0],[0][1],[0][2]. Or [n][k],[n-1][k],[0][k] -> [k][0],[k][n-1], [k][n].

# I just confused myself a lot.  A better way is apparently to reverse up to down, and then swap
# the symmetry.  I'm not sure on this one though.

def rotate(matrix: List[List[int]]) -> None:

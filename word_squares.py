""" 
with an algorithm that returns true if a sequence of words is a word square, do 0 -> length-k where 
k is 4 or length of word square. (0,1,2,3),(0,1,2,4),(0,1,2,5)

iterative: 
start with one word, for each letter of the word find another word that starts with that letter. ex. BALL -> BALL word(A) word(L) word(L) 

algo: first word = seq[0] = fword

j = number of words, iterating
k = length of words

seq[k][0..k] = seq[0..k][k]'

seq[0][0] = seq[0][0]
seq[0][1] = seq[1][0]
seq[0][2] = seq[2][0]
seq[0][3] = seq[3][0]

seq[1][0] = seq[0][1]
seq[1][1] = seq[1][1]
seq[1][2] = seq[2][1]
seq[1][3] = seq[3][1]

	0 1 2 3
      0 B A L L 
      1 A R E A
      2 L E A D
      3 L A D Y
"""
for j in range(0,len(seq)):
    for i in range(0,len(seq)):
	if(i!=j ):
            if(seq[j][i] != seq[i][j]):
	        return false
return true

"""
Why is this bad? 
Backtracking, goes over a lot of the same stuff multiple times which is wasteful.  This is O(n^2) time, O(1) space. 	
We could save runs in a dict which would improve runs as this size of the array increases. But calls aren't that inefficent, its the dbl loop.
"""

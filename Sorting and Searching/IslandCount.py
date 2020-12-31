# Link: https://www.pramp.com/challenge/yZm60L6d5juM7K38KYZ6

import collections
def get_number_of_islands(binaryMatrix):
  q = collections.deque()
  R = len(binaryMatrix)
  C = len(binaryMatrix[0])
  visited = set()
  numIslands = 0
  for r in range(0,R):
    for c in range(0,C):
      if(binaryMatrix[r][c] == 1 and (r,c) not in visited):
        numIslands += 1
        visited.add((r,c))
        q.append((r,c))
        while(q):
          c_r,c_c = q.popleft()
          neighbors = [(c_r + 1,c_c),(c_r-1,c_c),(c_r,c_c+1),(c_r,c_c-1)]
          for r_,c_ in neighbors:
            if(0 <= r_ < R and 0 <= c_ < C and (r_,c_) not in visited and binaryMatrix[r_][c_] == 1):
              visited.add((r_,c_))
              q.append((r_,c_))
  return numIslands

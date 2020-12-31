# Link: https://www.pramp.com/challenge/jKoA5GAVy9Sr9jGBjz04
def index_equals_value_search(arr):
  if(len(arr) == 0):
    return -1
  left = 0
  right = len(arr)-1
  while(left < right):
    midpoint = left + (right-left)//2
    if(arr[midpoint] == midpoint):

      if(midpoint - 1 > 0 and arr[midpoint - 1] == midpoint -1):
        right = midpoint
      else:
        return midpoint


    elif(arr[midpoint] < midpoint):
      left = midpoint
    else:
      right = midpoint

  return -1

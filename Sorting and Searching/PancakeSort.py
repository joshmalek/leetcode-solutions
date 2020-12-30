# Link: https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5LM1

# Not finished, not a good solution

def pancake_sort(arr):
  for i in range(0,len(arr)):
    if(min(arr[i:]) == arr[i]):
      continue
    else:
      index_min = arr.index(min(arr[i:]))
      new_arr = arr[i:]
      flip(new_arr,index_min)
      

def flip(arr,k):
  if(k >= len(arr)):
    arr = arr[::-1]
  else:
    return_array = arr[0:k+1]
    return_array = return_array[::-1]
    arr = return_array + arr[k:]
  return arr
def shifted_arr_search(shiftArr, num):
  #return shiftArr.index(num)

  pivot = 0
  left = 0
  right = len(shiftArr)-1
  while(left < right):
    mid = left + (right-left)//2
    if(mid == 0 or shiftArr[mid] < shiftArr[mid-1]):
      pivot = mid
      break
    elif(arr[mid] > arr[0]):
      left = mid
    else:
      right = mid
  print(pivot)
  if(pivot == 0 or num < shiftArr[0]):
    left = pivot
    right = len(shiftArr)-1
  else:
    left = 0
    right = pivot - 1
  
  print(left,right)
  while(left < right):
    mid = left + (right-left)//2
    print("midpoint:",mid)
    if(arr[mid] < num):
      left = mid
    elif(arr[mid] == num):
      return mid
    else:
      right = mid
  return -1
  
arr = [3,4,5,1,2]
print(shifted_arr_search(arr,2))
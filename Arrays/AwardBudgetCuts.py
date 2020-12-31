# Link: https://www.pramp.com/challenge/r1Kw0vwG6OhK9AEGAyWV

def find_grants_cap(grantsArray, newBudget):
  cap = float(newBudget) / float(len(grantsArray))
  grantsArray = sorted(grantsArray)
  for i in range(0, len(grantsArray)):
    if(grantsArray[i] < cap):
      remainder = cap - grantsArray[i]
      remaining_items = len(grantsArray)-i-1
      cap += float(remainder)/float(remaining_items)
  return round(cap,1)

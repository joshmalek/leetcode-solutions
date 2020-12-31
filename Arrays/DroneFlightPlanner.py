# Link: https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X
def calc_drone_min_energy(route):
  battery = 0
  min_bat = 0
  for i in range(1, len(route)):
    battery += route[i-1][2] - route[i][2]
    min_bat = min(min_bat, battery)
  return abs(min_bat)

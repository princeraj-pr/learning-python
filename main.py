picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

row = 0
while row < len(picture):
  for pixel in picture[row]:
    if pixel == 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()
  row += 1
  

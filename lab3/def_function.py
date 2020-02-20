from graph import *

def row ( y ):
  x = 40
  for i in range(5):
    circle(x, y, 20)
    x += 60
    
y = 40
for k in range(3):
  row(y)
  y += 60

run()

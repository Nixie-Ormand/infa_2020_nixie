from graph import *

# синий треугольник с шапочкой
def treug1 ( x, y, c, R, width, height ):
  brushColor(c)
  polygon([((x+0),(y+0)), ((x-width),(y-height)),
               ((x-width/2),(y+0)), ((x+0),(y+0))])
  circle((x-width),(y-height),R)
  
# зеленый треугольник с шапочкой
def treug2 ( x, y, c, R, width, height ):
  brushColor(c)
  polygon( [((x+0),(y+0)), ((x+width),(y-height)),
               ((x+width/2),(y+0)), ((x+0),(y+0))] )
  circle((x+width),(y-height),R)
  
# красный треугольник с шапочкой
def treug3 ( x, y, c, R, width, height ):
  brushColor(c)
  polygon( [((x-width/2),(y+0)), ((x+0),(y-height)),
               ((x+width/2),(y+0)), ((x-width/2),(y+0))] )
  circle((x+0),(y-height),R)

def crown (x,y,R, width, height):
  treug1 ( x, y, "blue", R, width, height)
  treug2 ( x, y, "green", R, width, height)
  treug3 ( x, y, "red", R, width, height)

R=15
width=50
height=100
x=200
y=200
penColor ( "black" )

crown (x,y,R, width, height)



run()


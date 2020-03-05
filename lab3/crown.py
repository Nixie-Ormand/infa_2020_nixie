from graph import *

# синий треугольник с шапочкой
def treug1 ( x, y, c ):
  brushColor(c)
  polygon( [(x,y), (x-25,y-70),
            (x+75,y), (x,y)] )
  circle(x-25,y-70,10)
  
# зеленый треугольник с шапочкой
def treug2 ( x, y, c ):
  brushColor(c)
  polygon( [(x,y), (x+80,y-70),
            (x+60,y), (x,y)] )
  circle(x+80,y-70,10)
  
# красный треугольник с шапочкой
def treug3 ( x, y, c ):
  brushColor(c)
  polygon( [(x,y), (x+25,y-80),
            (x+50,y), (x,y)] )
  circle(x+25,y-80,10)

penColor ( "black" )
treug1 ( 100, 150, "blue" )
treug2 ( 130, 150, "green" )
treug3 ( 120, 150, "red" )

run()


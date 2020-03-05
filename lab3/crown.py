from graph import *

# синий треугольник с шапочкой
def treug1 ( x, y, c, R ):
  brushColor(c)
  polygon( [(x,y), (x-25,y-70),
            (x+75,y), (x,y)] )
  circle(x-25,y-70,R)
  
# зеленый треугольник с шапочкой
def treug2 ( x, y, c, R ):
  brushColor(c)
  polygon( [(x,y), (x+80,y-70),
            (x+60,y), (x,y)] )
  circle(x+80,y-70,R)
  
# красный треугольник с шапочкой
def treug3 ( x, y, c, R ):
  brushColor(c)
  polygon( [(x,y), (x+25,y-80),
            (x+50,y), (x,y)] )
  circle(x+25,y-80,R)

R=20
penColor ( "black" )


treug1 ( 100, 150, "blue", R)
treug2 ( 130, 150, "green", R)
treug3 ( 120, 150, "red", R)

run()


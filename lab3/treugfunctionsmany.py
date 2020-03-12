from graph import *

#задаем вопрос, сколько в ряд 
number_of_crowns = input('Введите сколько корон в ряду: ')

number_of_rows = input('Введите сколько рядов: ')
      

# Функция - синий треугольник с шапочкой
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

# выше определим функции трех треугольников. Теперь определим функцию короны.

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

# комментарий crown (x,y,R, width, height)

# размножаем корону горизонтально, т.е. ставим N корон в ряд
def rowcrowns (x_ryad,y_ryad, step, number, width, height, R):
    for i in range (number):
        crown(x_ryad, y_ryad, R, width, height) 
        x_ryad+=step
ColumnNumber=int (number_of_rows)
y_column=50
for k in range (ColumnNumber):
    rowcrowns (40, y_column, 100,int (number_of_crowns), 25, 50, 7)
    y_column+=50

        

run()


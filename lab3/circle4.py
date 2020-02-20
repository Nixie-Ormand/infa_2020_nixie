from graph import *

x = 200; y = 300; r = 200
penColor('black')
a=250
b=250
c=0
N = 10

def CircleinProgression (x,y,r,N,a,b,c):

    # круг в прогрессии
    x = 400; y = 300; r = 200
    N = 10
    h = r//N
    hcolor=250//(N-1)
    brushColor(a,b,c)
    for i in range(10):
        circle (x,y,r)
        b=b-hcolor
        r-=h

   
CircleinProgression (x,y,r,N,a,b,c)


run()

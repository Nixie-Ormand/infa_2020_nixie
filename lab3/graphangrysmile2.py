
from graph import *

brushColor("green")
x=200; y=200
size=100
circle(x,y,size)

brushColor("yellow")
circle((x/1.25),(y/1.15),(size/5))
brushColor("yellow")
circle((x*1.25),(y/1.15),(size/5))

brushColor("black")
circle((x/1.25),(y/1.15),(size/10))
brushColor("black")
circle((x*1.25),(y/1.15),(size/10))

brushColor("yellow")
rectangle((x/1.25),(x+size/2.3),(x*1.25), (x+size/1.5))

brushColor("Black")
polygon([((size+size/10), size),
         ((x-size/10), (x-size/2)),
         ((x-size/5), (x-size/2.3)),
         ((size+size/20), (size+size/16.5))])
polygon([((x+size/5), (x-size/2)),
         ((x+size/1.11), (x-size/1.43)),
         ((x+(size-size/20)), (x-size/1.28)),
         ((x+size/6.6), (x-size/2.38))])

run()



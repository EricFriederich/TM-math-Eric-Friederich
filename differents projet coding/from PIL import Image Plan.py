import math
from PIL import Image 


chemin_image = r"C:\Users\Friederich\Documents\TM-math-Eric-Friederich\differents projet coding\carré.jpg"

image=Image.open(chemin_image)
x = (image.width)
y = (image.height)
Plan=Image.new('RGB',(x,y))
a=60

cx= math.ceil(x/2)
cy= math.ceil(y/2)
p = math.radians(a)

for i in range (x):
    for k in range (y):
        ox=i-cx
        oy=k-cy
        rx=int(ox*math.cos(p)-oy*math.sin(p)+cx)
        ry=int(ox*math.sin(p)+oy*math.cos(p)+cy)
        if 0<=rx<x and 0<=ry<x:
            color = image.getpixel((rx,ry))
            Plan.putpixel(( i,k),(color))
        


#nx=math.ceil((math.sqrt(2)/2)*(i+ox)-(math.sqrt(2)/2)*(k+oy))
#ny=math.ceil((math.sqrt(2)/2)*(i+ox)+(math.sqrt(2)/2)*(k+oy))



print(cx,cy)
Plan.show()
image.show()


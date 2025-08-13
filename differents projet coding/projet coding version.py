from PIL import Image
import math
import PIL


chemin_image = r"C:\Users\Friederich\Documents\TM-math-Eric-Friederich\differents projet coding\carré.jpg"
image = Image.open(chemin_image)
x = (image.width)
y = (image.height)
if x %2==0:
    image2=image.resize((x-200,y-200))
x2 = (image2.width)
y2 = (image2.height)
ox= math.ceil(x2/2)
oy= math.ceil(y2/2)

image_mod=Image.new('RGB',(x,y))

for i in range (0,x2):
    for k in range (0+100,y2):
        c = image2.getpixel((i,k))
        r = c[0]
        g = c[1]
        b = c[2]
        #nx=  math.ceil((math.sqrt(2)/2)*i-(math.sqrt(2)/2)*k)
        #ny=  math.ceil((math.sqrt(2)/2)*i+(math.sqrt(2)/2)*k)
        image_mod.putpixel((i,k),(r,g,b))






print(x2,y2)
#image.show()
image2.show()
image_mod.show()


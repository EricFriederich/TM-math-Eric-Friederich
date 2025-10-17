import math
from PIL import Image 
"""
J'ai importé l'outil de math afin de me simplifier les calcules trigonométriques.
J'ai aussi importé PIL qui me sera très utile à la manipulations d'images
"""
chemin_image = "image carré" #Je selectionne mon image dans mes dossiers

image=Image.open(chemin_image)
x = (image.width)
y = (image.height)
Plan=Image.new('RGB',(x,y))
"""
J'ouvre mon image et associe mon image ouverte à une variable, j'associe la longueure et la largeur de l'image ouverte à deux variables.
Je créé une nouvelle variable qui va représenter un plan noir de même longueure et largeur que mon image.
"""
a=60 #une variable qui dis à quel angles en degés  l'image va tourner

cx= math.ceil(x/2)
cy= math.ceil(y/2)
"""
Je fais deux nouvelles variables qui représentent la longeur et la largeur divisées par deux
"""

p = math.radians(a) #Je mets l'angle en Radian

for i in range (x): # Je parcours les pixels de mon image (tout les pixels d'une ligne puis on change de colone)
    for k in range (y):
        ox=i-cx #on fais une translations pour plustard faire tourner nos pixels autour de l'origine
        oy=k-cy
        rx=int(ox*math.cos(p)-oy*math.sin(p)+cx) # On fait tourner nos pixels autour de l'origine puis on fait la translation inverse pour replacer nos pixels
        ry=int(ox*math.sin(p)+oy*math.cos(p)+cy)
        if 0<=rx<x and 0<=ry<x:# on verifie si les coordonnées de nos pixels après rotation sont sur le plan. Si oui on on colorie le plan à la même couleur que le pixel de l'image qui à tourné, si non alors on fait rien
            color = image.getpixel((rx,ry))
            Plan.putpixel(( i,k),(color))
        




print(cx,cy)
Plan.show()
image.show()


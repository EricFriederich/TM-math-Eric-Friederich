from PIL import Image
import math

chemin_image = r"C:\Users\Friederich\Documents\TR-math-Eric-Friederich\differents_projet_coding\carre.jpg"
image = Image.open(chemin_image)
x = image.width
y = image.height

# Réduire légèrement la taille de l'image
image2 = image.resize((x-1, y-1))
x2 = image2.width
y2 = image2.height

# Calculer le centre de l'image
ox = math.ceil(x2/2)
oy = math.ceil(y2/2)

# Créer une nouvelle image
image_mod = Image.new("RGB", (x2, y2))

for i in range(0, x2):
    for k in range(0, y2):
        c = image2.getpixel((i, k))
        r = c[0]
        g = c[1]
        b = c[2]  # Correction: index 2 pour le bleu
        
        # Calcul des nouvelles coordonnées (exemple de symétrie centrale)
        nconrx = x2 - i - 1
        nconry = y2 - k - 1
        
        image_mod.putpixel((nconrx, nconry), (r, g, b))

# Sauvegarder ou afficher l'image résultante
image_mod.show()
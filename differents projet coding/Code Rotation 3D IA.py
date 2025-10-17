import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#  Définir les sommets d’un cube centré à l’origine 
points = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

#  Définir les arêtes (chaque paire d’indices à relier) 
edges = [
    (0,1), (1,2), (2,3), (3,0),  # face du bas
    (4,5), (5,6), (6,7), (7,4),  # face du haut
    (0,4), (1,5), (2,6), (3,7)   # montants verticaux
]

#  on va definir les angles de euler
alpha_z = np.deg2rad(60)  # rotation autour de Z
beta_y  = np.deg2rad(45)  # rotation autour de Y
gamma_x = np.deg2rad(23)  # rotation autour de X

# On va faire les 3 matrices de rotation élémentaires (autour de z,y et x)
Rz = np.array([
    [ np.cos(alpha_z), -np.sin(alpha_z), 0],
    [ np.sin(alpha_z),  np.cos(alpha_z), 0],
    [ 0,                0,               1]
])

Ry = np.array([
    [ np.cos(beta_y),  0, np.sin(beta_y)],
    [ 0,               1, 0],
    [-np.sin(beta_y),  0, np.cos(beta_y)]
])

Rx = np.array([
    [1, 0,                0               ],
    [0, np.cos(gamma_x), -np.sin(gamma_x)],
    [0, np.sin(gamma_x),  np.cos(gamma_x)]
])

# Rotation intrinsèque ZYX 
# On va d'abord multiplier X à Y puis le reste
R = Rz @ Ry @ Rx

#  Appliquer la rotation on applique la rotation
points_rotated = (R @ points.T).T

#  Affichage 3D 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Cube original (bleu clair pointillé)
for edge in edges:
    x = [points[edge[0], 0], points[edge[1], 0]]
    y = [points[edge[0], 1], points[edge[1], 1]]
    z = [points[edge[0], 2], points[edge[1], 2]]
    ax.plot(x, y, z, color='skyblue', linestyle='--', linewidth=1)

# Cube tourné (rouge)
for edge in edges:
    x = [points_rotated[edge[0], 0], points_rotated[edge[1], 0]]
    y = [points_rotated[edge[0], 1], points_rotated[edge[1], 1]]
    z = [points_rotated[edge[0], 2], points_rotated[edge[1], 2]]
    ax.plot(x, y, z, color='red', linewidth=2)

#  Mise en forme
ax.set_title("Rotation intrinsèque ZYX d’un cube centré à l’origine")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,1])

ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
ax.view_init(elev=25, azim=35)
plt.show()

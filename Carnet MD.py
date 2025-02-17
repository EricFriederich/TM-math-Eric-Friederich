import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.animation import FuncAnimation

def generate_cube():
    # Définition des sommets d'un cube
    vertices = np.array([
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ])
    
    # Définition des faces du cube
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]],
        [vertices[j] for j in [0, 3, 7, 4]],
        [vertices[j] for j in [1, 2, 6, 5]]
    ]
    return faces, vertices

def rotate_vertices(vertices, angle_x, angle_y, angle_z):
    # Matrices de rotation
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])
    Ry = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])
    Rz = np.array([
        [np.cos(angle_z), -np.sin(angle_z), 0],
        [np.sin(angle_z), np.cos(angle_z), 0],
        [0, 0, 1]
    ])
    
    R = Rx @ Ry @ Rz
    return np.dot(vertices, R.T)

def update(frame, poly3dcollection, ax, vertices):
    rotated_vertices = rotate_vertices(vertices, np.radians(frame), np.radians(frame), np.radians(frame))
    faces = [
        [rotated_vertices[j] for j in [0, 1, 2, 3]],
        [rotated_vertices[j] for j in [4, 5, 6, 7]],
        [rotated_vertices[j] for j in [0, 1, 5, 4]],
        [rotated_vertices[j] for j in [2, 3, 7, 6]],
        [rotated_vertices[j] for j in [0, 3, 7, 4]],
        [rotated_vertices[j] for j in [1, 2, 6, 5]]
    ]
    poly3dcollection.set_verts(faces)
    return poly3dcollection,

def animate_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    faces, vertices = generate_cube()
    poly3dcollection = art3d.Poly3DCollection(faces, alpha=0.5, edgecolor='k')
    ax.add_collection3d(poly3dcollection)
    
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    
    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), fargs=(poly3dcollection, ax, vertices), interval=50, repeat=True)
    plt.show()

animate_cube()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def problema_4_2():
  a, b, c, d = -33, -84, -9, 321
  p0 = np.array([0, 0, -23.67])
  p1 = np.array([-0.45, 0, 0])
  v = p1 - p0
  n = np.array([a, b, c])
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Plot the plane
  x, y = np.meshgrid(np.linspace(-10, 10, 10), 
                    np.linspace(-10, 10, 10))
  z = (-a*x - b*y - d) / c
  ax.plot_surface(x, y, z, alpha=0.5)

  # Plot the normal vector
  ax.quiver(p0[0], p0[1], p0[2], n[0], n[1], n[2], 
            length=50, normalize=True, color='r')

  # Set axis limits and labels
  ax.set_xlim(-10, 10)
  ax.set_ylim(-10, 10)
  ax.set_zlim(-30, 10)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  plt.show()


# Definir la función vectorial de dos variables
def f(x, y):
    return np.array([2*x/(x**2-y**2), -2*y/(x**2-y**2)])

# Crear una malla de puntos en el plano xy
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Evaluar la función vectorial en cada punto de la malla
Z = f(X, Y)

# Calcular el vector gradiente en cada punto de la malla
Gx, Gy = np.gradient(Z[0]), np.gradient(Z[1])

# Crear la figura y el objeto Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del vector gradiente
ax.plot_surface(X, Y, Z[0], cmap='coolwarm')
ax.plot_surface(X, Y, Z[1], cmap='coolwarm')

# Agregar el vector gradiente
ax.quiver(X, Y, Z[0], -Gx, -Gy, np.zeros_like(Gx), color='black')

# Configurar los límites de los ejes y la etiqueta de los ejes
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-10, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()

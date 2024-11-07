import matplotlib.pyplot as plt
import random as R
import numpy as np

# Numero de Generaciones Puntos aleatorios
n = 50000

# Coordenadas de los vértices del cuadrado de Sierpinski
vertex_coordinates = [[-200, -100], [-200, 300], [200, -100], [200, 300], [-200, 100], [0, -100], [0, 300], [200, 100]]

# Listas para almacenar las coordenadas de los puntos generados
x_coordinates = [vertex_coordinates[0][0]]
y_coordinates = [vertex_coordinates[0][1]]

# Generar puntos aleatorios dentro del cuadrado de Sierpinski
for i in range(n):
    r = R.randrange(8)
    x_coordinates.append((x_coordinates[-1] + 2 * vertex_coordinates[r][0]) / 3)
    y_coordinates.append((y_coordinates[-1] + 2 * vertex_coordinates[r][1]) / 3)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Generar colores aleatorios para cada punto

#Por ejemplo se puede usar:
# red, black, blue, green, yellow, cyan, magenta, white
colors = 'black'  # +1 para incluir el primer punto

# Dibujar los puntos con colores aleatorios
ax.scatter(x_coordinates, y_coordinates, s=0.1, color=colors, alpha=0.5)

# Configurar el título y mostrar el gráfico
ax.set(title=f'Sierpinski Square for {n} points')
plt.show()
import matplotlib.pyplot as plt
import random as R
import numpy as np

n = 10000

# Coordenadas de los vértices del triángulo equilátero
vertex_coordinates = [[-200.0, -100.0], [0.0, 200.0], [200.0, -100.0]]

# Listas para almacenar las coordenadas de los puntos generados
x_coordinates = [vertex_coordinates[0][0]]
y_coordinates = [vertex_coordinates[0][1]]

# Generar puntos aleatorios dentro del triángulo de Sierpinski
for i in range(n):
    r = R.randrange(3)
    x_coordinates.append((x_coordinates[-1] + vertex_coordinates[r][0]) / 2)
    y_coordinates.append((y_coordinates[-1] + vertex_coordinates[r][1]) / 2)

# Crear la figura y los ejes
fig, ax = plt.subplots()

#Por ejemplo se puede usar:
# red, black, blue, green, yellow, cyan, magenta, white
colors = 'black'  # +1 para incluir el primer punto

# Dibujar los puntos con colores aleatorios
ax.scatter(x_coordinates, y_coordinates, s=0.1, color=colors, alpha=0.5)

# Configurar el título y mostrar el gráfico
ax.set(title=f'Triángulo de Sierpinski para {n} puntos')
plt.show()
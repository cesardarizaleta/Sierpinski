import matplotlib.pyplot as plt
import numpy as np


# Parámetros del cuadrado de Sierpinski
nivel = 3  # Controla el número de subdivisiones
size = 1  # Tamaño del cuadrado inicial

def sierpinski_carpet(ax, x_start, y_start, size, level):
    if level == 0:
        # Dibujar el cuadrado base
        ax.fill(
            [x_start, x_start + size, x_start + size, x_start],
            [y_start, y_start, y_start + size, y_start + size],
            'black'
        )
    else:
        # Tamaño del subcuadrado
        new_size = size / 3
        
        # Dibujar los 8 subcuadrados recursivamente
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # Saltar el cuadrado central
                    continue
                sierpinski_carpet(ax, x_start + i*new_size, y_start + j*new_size, new_size, level - 1)

# Configuración del gráfico
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Dibujar el cuadrado de Sierpinski
sierpinski_carpet(ax, 0, 0, size, nivel)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Parámetros del cuadrado de Sierpinski
nivel = 3  # Controla el número de subdivisiones o profundidad del fractal
size = 1   # Tamaño del cuadrado inicial

def sierpinski_carpet(ax, x_start, y_start, size, level):
    if level == 0:
        # Dibujar el cuadrado base en el nivel más bajo de la recursión
        ax.fill(
            [x_start, x_start + size, x_start + size, x_start],
            [y_start, y_start, y_start + size, y_start + size],
            'black'  # Rellenar el cuadrado en color negro
        )
    else:
        # Calcular el tamaño de cada subcuadrado en este nivel
        new_size = size / 3
        
        # Dibujar los 8 subcuadrados de manera recursiva (omitimos el central)
        for i in range(3):         # Fila del subcuadrado
            for j in range(3):     # Columna del subcuadrado
                if i == 1 and j == 1:
                    # Saltar el cuadrado central para crear el "agujero"
                    continue
                # Llamada recursiva para el siguiente nivel de cada subcuadrado
                sierpinski_carpet(ax, x_start + i * new_size, y_start + j * new_size, new_size, level - 1)

# Configuración del gráfico
fig, ax = plt.subplots()         # Crear una figura y un eje
ax.set_aspect('equal')           # Mantener proporciones iguales
ax.axis('off')                   # Ocultar los ejes para una visualización limpia

# Dibujar el cuadrado de Sierpinski
sierpinski_carpet(ax, 0, 0, size, nivel)

# Mostrar el gráfico
plt.show()

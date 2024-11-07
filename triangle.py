import matplotlib.pyplot as plt  
import numpy as np  

# Nivel de detalle del fractal (cantidad de subdivisiones)
nivel = 5  

def sierpinski(x, y, size, level, color):  
   # Dibuja un triángulo equilátero en el nivel 0
   if level == 0:  
      # Dibuja el contorno de un triángulo equilátero con vértices en:
      # (x, y), (x+size, y), y (x+size/2, y+size*np.sqrt(3)/2)
      plt.plot([x, x+size, x+size/2, x], [y, y, y+size*np.sqrt(3)/2, y], color=color)  
   else:  
      # Llama recursivamente a la función para crear tres triángulos más pequeños
      # Triángulo inferior izquierdo
      sierpinski(x, y, size/2, level-1, color)  
      # Triángulo inferior derecho
      sierpinski(x+size/2, y, size/2, level-1, color)  
      # Triángulo superior
      sierpinski(x+size/4, y+size*np.sqrt(3)/4, size/2, level-1, color)  

def main():  
   # Configura el tamaño de la figura
   plt.figure(figsize=(8, 8))  
   # Define el color del triángulo (por ejemplo, 'r' para rojo)
   color = 'r'  
   # Llama a la función para dibujar el triángulo de Sierpinski
   sierpinski(0, 0, 1, nivel, color)  
   # Ajusta la escala para que el gráfico se vea proporcional
   plt.axis('equal')  
   # Desactiva los ejes para una visualización más limpia
   plt.axis('off')  
   # Muestra el gráfico
   plt.show()  

# Llama a la función principal para ejecutar el programa
main()

import matplotlib.pyplot as plt  
import numpy as np  

# Sierpinski triangle
#Cambiar para mas generaciones
nivel = 5
  
def sierpinski(x, y, size, level):  
   if level == 0:  
      plt.plot([x, x+size, x+size/2, x], [y, y, y+size*np.sqrt(3)/2, y], 'b-')  
   else:  
      sierpinski(x, y, size/2, level-1)  
      sierpinski(x+size/2, y, size/2, level-1)  
      sierpinski(x+size/4, y+size*np.sqrt(3)/4, size/2, level-1)  
  
def main():  
   plt.figure(figsize=(8, 8))  
   sierpinski(0, 0, 1, nivel)  
   plt.axis('equal')  
   plt.axis('off')  
   plt.show()  
  
main()
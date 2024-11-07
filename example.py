import matplotlib.pyplot as plt  
import numpy as np  
  
def sierpinski_square(x, y, size, level):  
   if level == 0:  
      plt.plot([x, x+size, x+size, x, x], [y, y, y+size, y+size, y], 'b-')  
   else:  
      sierpinski_square(x, y, size/2, level-1)  
      sierpinski_square(x+size/2, y, size/2, level-1)  
      sierpinski_square(x, y+size/2, size/2, level-1)  
      sierpinski_square(x+size/2, y+size/2, size/2, level-1)  
  
def main():  
   plt.figure(figsize=(8, 8))  
   sierpinski_square(0, 0, 1, 5)  
   plt.axis('equal')  
   plt.axis('off')  
   plt.show()  
  
main()
"""
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
"""
from math import sqrt

a = int(input("Ingrese el valor de 'A': " ))
b = int(input("Ingrese el valor de 'B': " ))
c = int(input("Ingrese el valor de 'C': " ))

if ((b**2) - (4*a*c)) <= 0:
    print("No se puede resolver la operacion")
else:
    x1 = (-b + (sqrt((b**2) - (4*a*c)))) / (2*a)    
    x2 = (-b - (sqrt((b**2) - (4*a*c)))) / (2*a)    
    print("La solucion es:", x1)
    print("La solucion es:", x2)


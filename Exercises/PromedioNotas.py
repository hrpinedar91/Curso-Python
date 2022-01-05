"""
Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
"""

p1 = float(input("Ingrese la nota de la 1° practica. "))
p2 = float(input("Ingrese la nota de la 2° practica. "))
p3 = float(input("Ingrese la nota de la 3° practica. "))

EP = float(input("Ingrese la nota del examen parcial. "))

EF = float(input("Ingrese la nota del examen final."))

PP = (p1 + p2 + p3) / 3

PROM = (PP + (2*EP) + (3*EF))/6

print("La nota final del estudiante es: ", PROM)


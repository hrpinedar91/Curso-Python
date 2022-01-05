"""
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
"""

name = input("Ingrese nombre. ")
age = input("Ingrese su edad. ")
sexo = input("Ingrese su sexo. ")

print("Te llamas: {} \nTu edad es: {}  \nEres: {}".format(name, age, sexo))
#ENTRADA DE DATOS

from cmath import sqrt 

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))




# PROCESO
x_1 = (-b + ((b**2 - (4*a*c))**(1/2))) / (2*a)
x_2 = (-b - ((b**2 - (4*a*c))**(1/2))) / (2*a)

# OPCIÓN 2
x_1 = (-b + pow((b**2 -(4*a*c)), (1/2))) / (2*a)
x_2 = (-b - pow((b**2 -(4*a*c)), (1/2))) / (2*a)

# SALIDA DE DATOS

print(f"x_1 es = {x_1}")

print(f"x_2 es = {x_2}")
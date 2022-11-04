#ENTRADA DE DATOS




calificación_1 = float(input("Escribe la primera calificación: "))
calificación_2 = float(input("Escribe la segunda calificación: "))
calificación_3 = float(input("Escribe la tercera calificación: "))


#PROCESO 

suma = calificación_1 + calificación_2 + calificación_3
promedio = suma / 3 

#SALIDA DE DATOS 

print(f"El promedio es = {round(promedio, 1)}")

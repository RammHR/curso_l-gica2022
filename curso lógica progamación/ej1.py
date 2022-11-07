#ENTRADA DE DATOS




calificación_1 = float(input("Escribe la primera calificación: "))
calificación_2 = float(input("Escribe la segunda calificación: "))
calificación_3 = float(input("Escribe la tercera calificación: "))


#PROCESO 

promedio = (calificación_1 + calificación_2 + calificación_3) / 3





#SALIDA DE DATOS 
if(promedio > 6 and promedio <= 10):
    print("Tu promedio es =", round(promedio , 1))
    print("APROBADO")
elif(promedio == 6):
    print("Tu promedio =", round(promedio , 1))
    print("APROBADO DE PANSASO")
elif(promedio >= 0 and promedio < 6):
    print("Tu promedio =", round(promedio , 1))
    print("REPROBADO")
else:
    print("PROMEDIO INVALIDO")
    
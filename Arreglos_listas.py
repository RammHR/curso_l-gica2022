#Arreglos (listas)
#Son variables especiales para coleccionar o almacenar uno o más valores
#de uno o más tipos de datos
#Sintaxis 

# arreglo_lista =[elementos/valores]

# Declarar o crear un arreglo
nombres =          ["Gerardo", "Saúl", "Ramón", "Daniel"]
# Índice (index)        0        1        2        3

edades      =      [26, 18, 22, 17]

#Índice (index)       0   1   2   3

arreglo_lista =    [5, 6.8, "Hola", True]
#Índice (index)     0   1     2      3

#OPERACIONES CON ARREGLOS O LISTAS

#Modificar un elemento del arreglo

nombres[2] = "Ramón Herrejón" 
edades[3] = 21

#Agregar un elemento al último arreglo
nombres.append("Eduardo")
edades.append(30)
arreglo_lista.append(False)



#Eliminar un elemento del arreglo

nombres.pop(1)
edades.pop(1)
arreglo_lista.pop(True)


#Vaciar el arreglo

nombres.clear()
edades.clear()
arreglo_lista.clear()


#Ordenar el arreglo 
nombres.sort()  #Ordenamiento Ascendente
edades.sort()     

nombres.reverse() #Ordenamiento Descendente

#SALIDA DE DATOS 

print("Nombre ", nombres)
print("Edades ", edades)
print("Arreglo ", arreglo_lista)



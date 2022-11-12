#FUNCIONES / PROCEDIMIENTOS / MÉTODOS / RUTINAS
# Son acciones o tareas a ejecutar (verbos en ar, er, ir)
#SINTAXIS:

# Def Nombre_de_la_Función ( Argumentos o Parámetros ):
# contenido de la función de la función
# return valor(es)



#Declarar las funciones 
def Sumar(num1, num2): #Obtener o recibir los parámetros
    return num1 + num2   #Retornar, Devolver, Retornar un valor

def Restar(a, b):
    resta = a - b 
    print("LA resta =", resta)

def Multiplicar(num3, num4):
    return num3 * num4

def Dividir(c, d):
    división = c / d
    print("la división =", división)


#Mandar a llamar o invocar las funciones
#Imprimir el resultado
print( "la suma =", Sumar(10,5))
Restar(50,20)
Restar(1, 2)
print("la multiplicación =", Multiplicar(5, 10))
Dividir(80, 10)


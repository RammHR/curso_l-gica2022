
nivel_de_agua = float(input("escribe el nivel de agua en metros:"))

#Salida de datos 

if(nivel_de_agua < 0):
    print("Fuga de cisterna")
elif(nivel_de_agua == 0):
    print("Encender bomba")
elif(nivel_de_agua > 0 and nivel_de_agua <= 2):
    print("Acelerar bomba")
elif(nivel_de_agua >= 2 and nivel_de_agua <= 4):
    print("Bomba trabajando")
elif(nivel_de_agua >= 4 and nivel_de_agua <= 6):
    print("Desacelerar bomba")
elif(nivel_de_agua == 6):
    print("Apagar bomba")
else:
    print("Desbordamiento de agua en cisterna")
    



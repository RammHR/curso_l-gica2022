#ENTRADA DE DATOS 

grados  =  float ( input ( "Escribe el número de grados: " ))


# PROCESO
farenheit_1  = (( 9  *  grados ) /  5 ) +  32
kelvin_1  =  grados  +  273.15
Celcius_1 = grados - 273.15


#SALIDA DE DATOS 

print(F"Grados Farenheit = {farenheit_1}")
print(F"Grados Kelvin = {kelvin_1}")
print(F"Grados Celcius = {Celcius_1}")

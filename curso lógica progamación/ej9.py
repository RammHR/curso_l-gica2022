#ENTRADA DE DATOS 
input("Contaduria RHR")
nombre = input("Ingresa tu nombre: ")
mes = input("Ingresa el nombre del mes: ")
días_laborados = float(input("Ingrsa el número de días del mes: "))
pagopdía = float(input("Ingresa el pago por día: "))



pago_base = días_laborados * pagopdía
iva_trasladado = pago_base * 0.16
subtotal = pago_base + iva_trasladado
iva_retenido = (2/3) * iva_trasladado
isr_retenido = pago_base * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido



print(F"El pago base ={pago_base}")
print(F"IVA TRASLADADO ={iva_trasladado}")
print(F"Subtotal ={subtotal}")
print(F"IVA_retenido ={iva_retenido}")
print(F"ISR_retenido ={isr_retenido}")
print(F"Pago neto ={pago_neto}")

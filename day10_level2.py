#Level 2 
#1._ Suma todos los números del 0 al 100 usando un bucle for
suma = 0
for i in range(0, 101):
    suma += i   
print("La suma de todos los numeros es ", suma)

#2._Suma todos los números pares e impares del 0 al 100 usando un bucle for
suma_pares = 0
suma_impares = 0    
for i in range(0, 101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print("La suma de los números pares es", suma_pares)
print("La suma de los números impares es", suma_impares)
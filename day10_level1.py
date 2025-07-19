#Level 1
#1._ Itera del 0 al 10 usando un bucle for, y haz lo mismo con while.
numbers=[0,1,2,3,4,5,6,7,8,9,10]
for numbers in numbers:
    print(numbers)
#Con While
contador = 0
while contador<=10:
    print(contador)
    contador = contador + 1

#2._- Itera del 10 al 0 usando for, y haz lo mismo con while.
numeros=[10,9,8,7,6,5,4,3,2,1,0]
for numeros in numeros:
    print(numeros)
#Con while 
count=10
while count>=0:
    print(count)
    count = count - 1

#3._- Haz un bucle que llame a print() siete veces para imprimir un triángulo de #.
for i in range(1,7):
    print('#' * i)

#4._- Usa bucles anidados para imprimir una cuadrícula de # como esta (8x8):
for fila in range(8):
    for columna in range(8):
        print('#', end='')
    print()

#5._ Imprime el siguiente patrón:
for y in range (11):
    print(f"{y} x {y} = {y*y}")

#6._ Itera a través de la lista e imprime los elementos
tecnologías=["Python", "Numpy", "Pandas", "Django", "Flask"]
for tecnologías in tecnologías:
    print(tecnologías)

#7._ Itera del 0 al 100 e imprime solo los números pares
for d in range(0,101):
    if d % 2 == 0:
        print(d)

#8._Itera del 0 al 100 e imprime solo los números impares
for d in range(0, 101):
    if d % 2 != 0:
        print(d)
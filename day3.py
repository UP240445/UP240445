edad = 18
peso = 85
complex_number = 18

base = 20
altura = 15
area = base * altura
print(area)

lado_a = 10
lado_b = 20
lado_c = 30
perimetro = lado_a + lado_b + lado_c
print(perimetro)

longitud = 10
ancho = 5
area_rectangulo = longitud * ancho
print(area_rectangulo)

radius = 5
area_circulo = 3.14 * (radius ** 2)
print(area_circulo)

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(slope)
print(distancia)

for x in (-6, 1):  
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")

print(len("python"))   
print(len("dragon"))   
print(len("python") != len("dragon"))

print('on' in 'python' and 'on' in 'dragon')

oracion = "espero que este curso sea de jargon."
print("jargon" in oracion) 
print('on' in 'python')   
print('on' in 'dragon')   
print('on' in 'python' and 'on' in 'dragon') 

longitud = len("python")
float_longitud = float(longitud)
string_longitud = str(longitud)

numero = 8
if numero % 2 == 0:
    print("par")
else:
    print("impar")

resultado = 7 // 3
convertido = int(2.7)
print(resultado)

print(type(10) == type(10))

print(int(9.8) == 10)

horas = 40
pago_por_hora = 28

pago_total = horas * pago_por_hora
print("pago total:", pago_total)

segundo_por_año = 60 * 60 * 24 * 365

años_vividos = int(input("ingrese los años vividos: "))

tiempo_vivido = segundo_por_año * años_vividos
print("has vivido", tiempo_vivido, "segundos.")

for i in range(1, 6):
    print(i, 1, i, i*2, i*3)
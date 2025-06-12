import math

num_one=5
num_two=4
total= num_one + num_two
diff= num_two - num_one
product= num_two*num_one
division= num_one/num_two
remainder=num_two%num_one
exp=num_one^num_two
floor_division=num_one//num_two


radius=30
area_of_circle=math.pi*(radius**2)
print("El área del circulo es ", area_of_circle)
circum_of_circle=2*math.pi*(radius**2)
print("La circunferencia del circulo es", circum_of_circle)

radius=float(input("Ingresa el radio del círculo: "))
area_of_circle=math.pi*(radius**2)
print("El área del circulo es", area_of_circle)


nombre=input("Escribe un primer nombre: ")
apellido=input("Escribe un apellido: ")
país=input("Escribe un país: ")
edad=input("Escribe una edad: ")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("País:", país)
print("Edad:", edad)
#Palabras Resevadas

help("keywords")
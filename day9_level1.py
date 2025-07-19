#1._Obtén la edad del usuario usando input("Enter your age: "). Si el usuario tiene 18 años o más, da el mensaje: Eres lo suficientemente mayor para conducir. Si es menor de 18, dile cuántos años le faltan para poder conducir. Salida:
edad=int((input("Ingresa tu edad:  ")))
if edad >= 18:
    print("Eres lo suficiente mayor para conducir")
else: 
    print("Te faltan", 18 - edad , "años para poder conducir")
#2._Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (yo o tú)? Usa input("Enter your age: ") para obtener la edad como entrada. Puedes usar una condición anidada para imprimir 'año' si la diferencia de edad es 1, 'años' para diferencias mayores, y un texto personalizado si my_age = your_age. Salida:
my_age= 24
your_age= int((input("Ingresa tu edad: ")))
if my_age > your_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print("Eres mayor que yo por 1 año")
    else:
        print(f"Eres mayor que yo por {diferencia} años")
elif my_age < your_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print("Soy mayor que tú por 1 año")
    else:
        print(f"Soy mayor que tú por {diferencia} años")
else:
    print("Tenemos la misma edad")
#3._Obtén dos números del usuario usando input. Si a es mayor que b, muestra "a es mayor que b", si a es menor que b, muestra "a es menor que b", si no, muestra "a es igual a b". Salida:
a = int((input("Ingresa el primer número: ")))
b = int((input("Ingresa el segundo número: ")))
if a > b:
    print("a es mayor que b")
elif a < b: 
    print("a es menor que b")
else:
    print(" a es igual a b")
#Level 2
#1._Escribe un código que asigne calificaciones a los estudiantes de acuerdo a sus puntajes:
calificacion= int((input("Ingrese la calificación del estudiante: ")))
if 80 <= calificacion <= 100:
    print("La calificación del estudiante es una A")
elif 70 <= calificacion <= 79:
    print("La calificación del estudiante es una B")
elif 60 <= calificacion <= 69:
    print("La calificación del estudiante es un C")
elif 50 <= calificacion <= 59:
    print("La calificación del estudiante es una D")
elif 0 <= calificacion <= 49:
    print("La calificación del estudiante es una F")
else:
    print("Puntuaje inválido. Debe estar entre 0 y 100")
#2._Verifica si la estación es Otoño, Invierno, Primavera o Verano. Si el usuario ingresa: septiembre, octubre o noviembre, la estación es Otoño. Diciembre, enero o febrero, la estación es Invierno. Marzo, abril o mayo, la estación es Primavera. Junio, julio o agosto, la estación es Verano.
mes= input("Ingrese un mes de año: ").lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    estacion="Otoño"
    print(f"La estación correspondiente a {mes.capitalize()} es: {estacion}.")

elif mes in ["diciembre", "enero", "febrero"]:
    estacion="Invierno"
    print(f"La estación correspondiente a {mes.capitalize()} es: {estacion}.")

elif mes in["marzo", "abril", "mayo"]:
    estacion="Primavera"
    print(f"La estación correspondiente a {mes.capitalize()} es: {estacion}.")

elif mes in["junio", "julio", "agosto"]:
    estacion="Verano"
    print(f"La estación correspondiente a {mes.capitalize()} es: {estacion}.")

else:
    estacion="Mes no valido"
    print(f"La estación correspondiente a {mes.capitalize()} es: {estacion}.")
#3._Si una fruta no existe en la lista, agrégala a la lista y muestra la lista modificada. Si la fruta existe, imprime 'Esa fruta ya existe en la lista'.
fruits=["banana", "orange", "mango", "lemon"]
fruta_nueva=input("Ingresa una fruta: ")
if fruta_nueva in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta_nueva)
    print("Lista modificada: ", fruits)
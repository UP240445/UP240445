#Level 3
#1._Convierte las edades a un conjunto y compara la longitud de la lista y del conjunto, ¿cuál es mayor?
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades_unicas = set(edades)

print("Lista original:", edades)
print("Conjunto sin duplicados:", edades_unicas)
print("Longitud de la lista:", len(edades))
print("Longitud del conjunto:", len(edades_unicas))

if len(edades) > len(edades_unicas):
    print("La lista tiene más elementos (porque incluye duplicados).")
elif len(edades) < len(edades_unicas):
    print("El conjunto tiene más elementos (¡algo muy raro!).")
else:
    print("Ambos tienen la misma longitud.")

#2._ Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
#Cadena: Una cadena es una secuencia de caracteres inmutable, utilizada para representar texto. Por ejemplo, "Hola Mundo".
#Lista: Una lista es una colección ordenada y mutable de elementos, que puede contener duplicados. Por ejemplo, [1, 2, 3, 4].
#Tupla: Una tupla es una colección ordenada e inmutable de elementos, que también puede contener duplicados. Por ejemplo, (1, 2, 3, 4).
#Conjunto: Un conjunto es una colección no ordenada de elementos únicos, sin duplicados. Por ejemplo, {1, 2, 3, 4}.                             

#Soy profesor y me encanta inspirar y enseñar a las personas. ¿Cuántas palabras únicas se han usado en la oración? Usa los métodos split() y set para obtener las palabras únicas.
oracion = "Soy profesor y me encanta inspirar y enseñar a las personas."
palabras=oracion.split()
unicas=set(palabras)
cantidad=len(unicas)
print("Palabras únicas", unicas)
print("Cantidad de palabras únicas", cantidad)
#Level 2
#1._Desempaquetar hermanos y padres desde la tupla de miembros de la familia
hermanas=("janis", "maria", "luz")
hermanos=("Leonardo", "jorge", "Angel")
hermanas_hermanos=hermanas+hermanos
conv_lista=list(hermanas_hermanos)
conv_lista[0:1]="liz", "hector"
tupla_modificada=tuple(conv_lista)
print(hermanas)
print(hermanos)
print(tupla_modificada[0:2])
print(hermanas_hermanos)
#2._Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
fruits=("pera", "sandía", "manzana")
vegetables=("elote", "zanahoria", "brocoli")
animal_products=("huevo", "leche", "carne")
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
#3._Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt=list(food_stuff_tp)
#4._Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n=len(food_stuff_lt)
if n % 2 == 0:
    del food_stuff_lt[n//2 - 1 : n//2 + 1]
else:
    del food_stuff_lt[n//2]
print(food_stuff_lt)
#5._Separe los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
print(food_stuff_lt[0:3]) 
print(food_stuff_lt[-3:])
#6._Eliminar la tupla food_staff_tp por completo
del food_stuff_tp
#7._Comprobar si un elemento existe en una tupla:

#8
#.Check if 'Estonia' is a nordic country
#.Check if "Iceland" is a nordic country
nordic_countries=('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia es un país nordico", "Estonia" in nordic_countries)
print("Islandia es un páis nordico", "Islandia" in nordic_countries)
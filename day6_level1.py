#1._ Crea una tuple vacía
tupla_vacía=()
#2._ Crea tuplas con nombres de hermanas y hermanos
hermanas=("janis"   , "maria", "luz")
hermanos=("Leonardo", "jorge", "Angel")
print(hermanas)
print(hermanos)
#3._Unir las tuplas de hermanos y hermanas en una sola llamada 'hermanos_y_hermanas'
hermanas_hermanos=hermanas+hermanos
print(hermanas_hermanos)
#4._¿Cuántos hermanos tienes?
print("Tengo", len(hermanas_hermanos), "hermanos. ")
#5._Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
conv_lista=list(hermanas_hermanos)
conv_lista[0:1]="liz", "hector"
tupla_modificada=tuple(conv_lista)
print(tupla_modificada)
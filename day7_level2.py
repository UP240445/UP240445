#Level 2
it_companies={"facebook", "Google", "Microsoft" , "Apple"}
#1._Unir A y B
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
union=A.union(B)
print(union)
#2._Encuentra la interseccion entre A y B 
interseccion=A.intersection(B)
print(interseccion)
#3._ ¿Es A un subconjunto de B?
print(A.issubset(B))
#4._ ¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))
#5._ Une A con B y B con A 
unionA= A.union(B), B.union(A)
print(unionA)
#6._ ¿Cuál es la diferencia simétrica entre A y B?
no_repiten= A.symmetric_difference(B)
print(no_repiten)
#7._ Elimina las listas completas
del it_companies
print(it_companies)
#Level 1
#1._ Encuentra la longitud del conjunto it_companies
it_companies={"facebook", "Google", "Microsoft" , "Apple"}
longitud=len(it_companies)
print(longitud)
#2._Agrega twitter a it_compamies
it_companies.add("Twitter")
print(it_companies)
#3._ Inserta múltiples empresas de tecnología en el conjunto it_companies
it_companies.update(["Tesla", "Copilot", "Space X"])
print(it_companies)
#4._ Elimina una de las empresas del conjunto it_companies
it_companies.remove("Tesla")
print(it_companies)
#5._ - ¿Cuál es la diferencia entre remove y discard?
#La diferencia es que si en discard el valor no existe no lanza error y en remove si 
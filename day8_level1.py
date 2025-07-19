#Level 1
#1._ Crea un diccionario vacío llamado dog
dog={}
#2._Agrega name, color, breed, legs, age al diccionario dog.
dog["name"] = "jorgi"
dog["color"] = "Negro con blanco"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 2
print(dog)
#3._Crea un diccionario llamado student y agrega first_name, last_name, gender, age, marital status, skills, country, city y address como claves para el diccionario.
student={"first_name": "leo" ,
         "last_name": "gomez" , 
         "gender": "Masculino" , 
         "age": "19 años" , 
         "marital_status": "Soltero" , 
         "skills": ["Linux", "Python", "technical writing"],
          "country": "México" ,
           "city": "Aguascalientes" ,
            "address": "vistas de oriente, gran canon 145 #514" ,
              }
print(student)
#4._Obtén la longitud del diccionario student 
print(len(student))
#5._Obtén el valor de skills y verifica el tipo de dato, debe ser una lista.
print(student["skills"])
print(type(student["skills"]))
#6._Modifica los valores de skills agregando una o dos habilidades
student["skills"].append("JavaScript")
student["skills"].append("HTML")            
print(student["skills"])
#7._Obtén las claves del diccionario como una lista
claves=list(student.keys())
print(claves)
#8._Obtén los valores del diccionario como una lista
valores=list(student.values())
print(valores)
#9._Cambia el diccionario a una lista de tuplas usando el método items()
tuplas=list(student.items())
print(tuplas)
#10._Elimina uno de los elementos del diccionario
del student["skills"]
print(student)
#11._Elimina uno de los diccionarios
del dog
print(dog)
#Level 3
#1._ Extrae todos los países que contienen la palabra 'land'
countries = ['Finland', 'Ireland', 'Switzerland', 'Iceland', 'New Zealand', 'Thailand']
countries_with_land = [country for country in countries if 'land' in country]           
print(countries_with_land)
#2._ Invierte el orden de la lista de frutas usando un bucle
fruits = ['banana', 'orange', 'mango', 'lemon'] 
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])   
print(reversed_fruits)

#3._Ve a la carpeta de datos y usa el archivo countries_data.py
countries_data = [
    {
        'name': 'China',
        'population': 1409517397,
        'languages': ['Chinese']
    },
    {
        'name': 'India',
        'population': 1339180127,
        'languages': ['Hindi', 'English']
    },
    {
        'name': 'USA',
        'population': 324459463,
        'languages': ['English']
    },
    # ... más países
]
#._Cuál es el número total de idiomas en los datos?
total_languages = set()
for country in countries_data:
    total_languages.update(country['languages'])
print(f"Total unique languages: {len(total_languages)}")
#._Encuentra los diez idiomas más hablados según los datos.
from collections import Counter
language_count = Counter()
for country in countries_data:
    for language in country['languages']:
        language_count[language] += 1
most_common_languages = language_count.most_common(10)
print("Los lenguajes más comunes son: ", most_common_languages)
#._Encuentra los 10 países más poblados del mundo.
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_10_populated_countries = sorted_countries[:10]          
print("Los 10 países más poblados son: ")
for country in top_10_populated_countries:
    print(f"{country['name']} - Population: {country['population']}")   
#Level 3
#1._
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person:
    skills=person["skills"]
    en_medio=len(skills)//2
    print(f"Habilidad de en medio:{skills[en_medio]}")

if "skills" in person:
    existe_python="Python" in person["skills"]
    print(f"Tiene la habilidad Python: {existe_python}")


if 'skills' in person:
    s = set(person['skills'])  
    if s == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(s):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(s):
        print("He is a fullstack developer")
    else:
        print("unknown title")

#2._

if person.get('is_marred') and person.get('country') == 'Finland':
    nombre = f"{person['first_name']} {person['last_name']}"
    print(f"{nombre} lives in Finland. He is married.")
class Person:
    people = {}

<<<<<<< HEAD
    def __init__(self, name, age):
=======
    def __init__(self, name: str, age: int) -> None:
>>>>>>> f5e8933 (Corrigir estilo com list comprehension e W293)
        self.name = name
        self.age = age
        Person.people[name] = self


<<<<<<< HEAD
def create_person_list(people_data):
    person_list = []
    
    # Primeira passada: cria todas as instâncias e as adiciona à lista
    for data in people_data:
        person = Person(data["name"], data["age"])
        person_list.append(person)
        
    # Segunda passada: vincula os cônjuges (wife ou husband) usando o dicionário de classe
    for data in people_data:
        person = Person.people[data["name"]]
        
        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]
            
        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]
            
=======
def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(name=person_data["name"], age=person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if person_data.get("wife") is not None:
            person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            person.husband = Person.people[person_data["husband"]]

>>>>>>> f5e8933 (Corrigir estilo com list comprehension e W293)
    return person_list

class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


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
            
    return person_list

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    
    # 1. Crear todas las instancias básicas de Person
    for person_data in people:
        person = Person(name=person_data["name"], age=person_data["age"])
        person_list.append(person)
        
    # 2. Asignar los vínculos de matrimonio usando el diccionario de clase
    for person_data, person in zip(people, person_list):
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]
            
    return person_list

class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    lista_of_people = []
    for person in people:
        obj_person = Person(person["name"], person["age"])
        lista_of_people.append(obj_person)
        if "wife" in person.keys():
            obj_person.wife = person["wife"]
        else:
            obj_person.husband = person["husband"]

    for index, people in enumerate(lista_of_people):
        if "wife" in people.keys() and people["wife"] is not None:
            lista_of_people[index] = people.wife = Person.people[people.wife]
        if "husband" in people.keys() and people["husband"] is not None:
            lista_of_people[index] = people.husband = Person.people[people.husband]
    return lista_of_people

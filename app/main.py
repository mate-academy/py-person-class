# from os import name
# from xml.sax.handler import property_lexical_handler


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        pessoa = Person(person["name"], person["age"])
        person_list.append(pessoa)
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]
            husband.wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            wife = Person.people[person["name"]]
            wife.husband = husband

    return person_list

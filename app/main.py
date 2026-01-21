

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dict: list) -> list:
    Person.people = {}
    people_list = []

    for pers in people_dict:
        person = Person(pers["name"], pers["age"])
        people_list.append(person)

    for pers in people_dict:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            person.wife = Person.people[pers["wife"]]
        elif "husband" in pers and pers["husband"] is not None:
            person.husband = Person.people[pers["husband"]]

    return people_list

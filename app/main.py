class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:

    Person.people = {}
    person_list = {}

    for pers in people:
        persons = Person(pers["name"], pers["age"])
        person_list[pers["name"]] = persons

    for pers in people:
        persons = person_list[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            persons.wife = person_list[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            persons.husband = person_list[pers["husband"]]

    Person.people = person_list

    return list(person_list.values())

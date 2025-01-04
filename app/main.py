class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        Person.people[name] = self
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    list_people = []

    for pers in people:
        list_people.append(Person(pers["name"], pers["age"]))

    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
            Person.people[pers["wife"]].husband = Person.people[pers["name"]]
    return list_people

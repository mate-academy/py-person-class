class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for pers in people:
        person_list.append(Person(pers["name"], pers["age"]))
    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            Person.people[pers["name"]].husband = \
                Person.people[pers["husband"]]
    return person_list

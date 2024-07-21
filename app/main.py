class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for pers in people:
        if pers["name"] not in Person.people:
            Person(pers["name"], pers["age"])

    for pers in people:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            person.wife = Person.people[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            person.husband = Person.people[pers["husband"]]

    return [Person.people[pers["name"]] for pers in people]

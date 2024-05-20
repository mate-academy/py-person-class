class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for pers in people:
        Person(pers["name"], pers["age"])

    for pers in people:
        if "wife" in pers and pers["wife"]:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
        if "husband" in pers and pers["husband"]:
            Person.people[pers["name"]].husband = Person.people[pers["husband"]]

    return list(Person.people.values())

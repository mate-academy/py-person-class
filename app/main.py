class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:

    people_list = [Person(person["name"], person["age"]) for person in people]
    for preson in people:
        if preson.get("wife"):
            Person.people[preson["name"]].wife \
                = Person.people[preson["wife"]]
        if preson.get("husband"):
            Person.people[preson["name"]].husband \
                = Person.people[preson["husband"]]
    return people_list

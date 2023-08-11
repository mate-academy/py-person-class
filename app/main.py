from __future__ import annotations


class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        partner = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            partner.wife = wife
        elif "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            partner.husband = husband

    return person_list

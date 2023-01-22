# from __future__ import annotations


class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list) -> list:
    humans = []
    for person in persons:
        name = person["name"]
        age = person["age"]
        human = Person(name, age)
        humans.append(human)
    for person, human in zip(persons, humans):
        if "wife" in person:
            if person["wife"] is not None:
                human.wife = Person.people[person["wife"]]
        else:
            if person["husband"] is not None:
                human.husband = Person.people[person["husband"]]
    return humans

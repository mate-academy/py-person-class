# from __future__ import annotations


class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list) -> list:
    humans = []
    for dictionary in persons:
        name = dictionary["name"]
        age = dictionary["age"]
        human = Person(name, age)
        humans.append(human)
    for dictionary, human in zip(persons, humans):
        if "wife" in dictionary:
            if dictionary["wife"] is not None:
                human.wife = Person.people[dictionary["wife"]]
        else:
            if dictionary["husband"] is not None:
                human.husband = Person.people[dictionary["husband"]]
    return humans

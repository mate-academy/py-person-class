from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for p in people:

        if "wife" in p and p["wife"] is not None:
            Person.people[p["name"]].wife = Person.people[p["wife"]]

        if "husband" in p and p["husband"] is not None:
            Person.people[p["name"]].husband = Person.people[p["husband"]]

    return people_list

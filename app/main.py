from __future__ import annotations


class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_example = Person.people[person["name"]]
        if person.get("wife"):
            person_example.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_example.husband = Person.people[person["husband"]]

    return list(Person.people.values())

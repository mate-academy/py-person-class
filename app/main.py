from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> Person:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"])
                   for person in people]

    for i, person in enumerate(person_list):
        if people[i].get("wife"):
            person.wife = person.people[
                people[i]["wife"]
            ]
        elif people[i].get("husband"):
            person.husband = person.people[
                people[i]["husband"]
            ]

    return person_list

from __future__ import annotations


class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    @classmethod
    def find_by_name(cls, name: str) -> Person | None:
        return cls.people[name]


def create_person_list(people: list) -> list[Person]:
    for p in people:
        Person(p["name"], p["age"])

    for p in people:
        if "wife" in p and p["wife"]:
            person = Person.find_by_name(p["name"])
            person.wife = Person.find_by_name(p["wife"])
        elif "husband" in p and p["husband"]:
            person = Person.find_by_name(p["name"])
            person.husband = Person.find_by_name(p["husband"])

    return list(Person.people.values())

from __future__ import annotations
from typing import Optional


class Person:

    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    def add_wife(self, wife: Optional[str]) -> None:
        if wife is not None:
            self.wife = self.people[wife]

    def add_husband(self, husband: Optional[str]) -> None:
        if husband is not None:
            self.husband = self.people[husband]


def create_person_list(
        people: list[dict[str, str | int | None]]
) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person, properties in zip(person_list, people):
        if properties.get("wife") is not None:
            person.add_wife(properties["wife"])
        elif properties.get("husband") is not None:
            person.add_husband(properties["husband"])

    return person_list

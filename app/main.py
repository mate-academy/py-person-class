from __future__ import annotations


class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    @classmethod
    def find_by_name(cls, name: str) -> Person | None:
        return cls.people.get(name)


def create_person_list(people: list) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "wife" in person and person["wife"]:
            person_obj = Person.find_by_name(person["name"])
            person_obj.wife = Person.find_by_name(person["wife"])
        elif "husband" in person and person["husband"]:
            person_obj = Person.find_by_name(person["name"])
            person_obj.husband = Person.find_by_name(person["husband"])

    return list(Person.people.values())

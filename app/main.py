# from __future__ import annotations


class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    @property
    def wife(self) -> people:
        return self.people.get(self._wife)

    @wife.setter
    def wife(self, name: str) -> None:
        self._wife = name

    @property
    def husband(self) -> people:
        return self.people.get(self._husband)

    @husband.setter
    def husband(self, name: str) -> None:
        self._husband = name


def create_person_list(persons: list) -> list:
    humans = []
    for dictionary in persons:
        name = dictionary["name"]
        age = dictionary["age"]
        human = Person(name, age)
        if "wife" in dictionary:
            if dictionary["wife"] is not None:
                human.wife = dictionary["wife"]
        else:
            if dictionary["husband"] is not None:
                human.husband = dictionary["husband"]

        humans.append(human)
    return humans


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

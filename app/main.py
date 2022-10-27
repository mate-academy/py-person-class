from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.add_people(self)

    @classmethod
    def add_people(cls, person: Person) -> None:
        cls.people[person.name] = person


def create_person_list(people: list) -> list[Person]:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        wife = person.get("wife")
        if wife in Person.people:
            cur_person = Person.people[person["name"]]
            cur_person.wife = Person.people[wife]

        husband = person.get("husband")
        if husband in Person.people:
            cur_person = Person.people[person["name"]]
            cur_person.husband = Person.people[husband]

    return persons

from typing import List, Dict


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: List[Dict]) -> List[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person.husband = Person.people[person["husband"]]
    return person_list

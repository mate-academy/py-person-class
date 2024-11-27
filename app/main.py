from typing import List, Dict


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    people = {}

    def add_to_people(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: List[Dict]) -> List[Person]:
    person_list = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person.add_to_people()
        person_list.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            spouse_name = person_dict["wife"]
            spouse = Person.people[spouse_name]
            person.wife = spouse
        if "husband" in person_dict and person_dict["husband"] is not None:
            spouse_name = person_dict["husband"]
            spouse = Person.people[spouse_name]
            person.husband = spouse

    return person_list

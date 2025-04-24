from __future__ import annotations


class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person(self)
    @classmethod
    def add_person(cls, obj: Person):
        cls.people[obj.name] = obj

def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]
    return persons



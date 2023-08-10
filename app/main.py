from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    print(len(Person.people))
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person = Person.people[name]
            wife = Person.people[wife_name]
            person.wife = wife

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person = Person.people[name]
            husband = Person.people[husband_name]
            person.husband = husband
    return person_list

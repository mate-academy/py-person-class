from typing import List, Dict, Any


class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: List[Dict[str, Any]]) -> List[Person]:
    Person.people = {}

    person_instances: List[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_dicts
    ]

    for person_data in people_dicts:
        current_person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name:
            current_person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name:
            current_person.husband = Person.people[husband_name]

    return person_instances

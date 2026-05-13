from __future__ import annotations
from typing import List, Dict, Any, Optional


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: List[Dict[str, Any]]) -> List[Person]:
    person_instances = [
        Person(p["name"], p["age"]) for p in people_data
    ]

    for person_dict in people_data:
        name = person_dict["name"]
        current_instance = Person.people[name]

        spouse_name: Optional[str] = (
            person_dict.get("wife") or person_dict.get("husband")
        )

        if spouse_name:
            spouse_attr = "wife" if "wife" in person_dict else "husband"
            setattr(current_instance, spouse_attr, Person.people[spouse_name])

    return person_instances

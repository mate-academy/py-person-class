from __future__ import annotations
from typing import Dict, List, Optional, Any


class Person:

    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        # Add person to the class attribute dictionary
        Person.people[name] = self


def create_person_list(people_list: List[Dict[str, Any]]) -> List[Person]:
    Person.people.clear()  # Clear any previous data
    result: List[Person] = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        result.append(Person(name, age))

    # Link wives and husbands
    for person_dict in people_list:
        name = person_dict["name"]
        person_obj = Person.people[name]

        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person_obj

        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person_obj

    return result

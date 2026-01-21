from __future__ import annotations
from typing import List, Dict, Any


class Person:
    """
    Represents a person and stores all created instances in a class attribute
    for easy lookup.
    """
    people: Dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a Person instance and adds it to the class-level
        'people' dictionary.
        """
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation
        of the Person object.
        """
        return f'Person(name="{self.name}", age={self.age})'


def create_person_list(people_data: List[Dict[str, Any]]) -> List[Person]:
    """
    Creates a list of Person instances from a list of dictionaries,
    linking spouses together.
    """
    Person.people.clear()

    # Checklist Item #3: Use a list comprehension to create instances.
    person_instances = [
        Person(name=p["name"], age=p["age"]) for p in people_data
    ]

    for person_instance, person_info in zip(person_instances, people_data):
        # Checklist Item #4: Use .get() to safely access spouse names.
        wife_name = person_info.get("wife")
        husband_name = person_info.get("husband")

        # Avoid KeyError: Safely look up spouse instance using .get().
        if wife_name and (wife_instance := Person.people.get(wife_name)):
            person_instance.wife = wife_instance
        elif husband_name and (husband_instance := Person.people.get(husband_name)):
            person_instance.husband = husband_instance

    return person_instances

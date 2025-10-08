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

        Args:
            name: The name of the person.
            age: The age of the person.
        """
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the Person object.
        """
        return f"Person(name=\"{self.name}\", age={self.age})"


def create_person_list(people_data: List[Dict[str, Any]]) -> List[Person]:
    """
    Creates a list of Person instances from a list of dictionaries,
    linking spouses together.

    This function operates in two passes:
    1. It creates all Person instances, which populates the Person.people
       class attribute.
    2. It iterates through the data again to set the wife/husband attributes,
       using the now-complete Person.people dictionary for lookups.

    Args:
        people_data: A list of dictionaries, where each dictionary
                     represents a person.

    Returns:
        A list of fully configured Person instances.
    """
    # Clear the class attribute to ensure no data from previous
    # runs interferes.
    Person.people.clear()
    person_instances = []

    # First pass: Create all Person objects.
    # This populates the Person.people dictionary.
    for person_info in people_data:
        person_instances.append(
            Person(name=person_info["name"], age=person_info["age"])
        )

    # Second pass: Link spouses using the now-complete Person.people
    # registry.
    for i, person_info in enumerate(people_data):
        current_person = person_instances[i]
        if "wife" in person_info and person_info["wife"]:
            wife_name = person_info["wife"]
            current_person.wife = Person.people[wife_name]
        elif "husband" in person_info and person_info["husband"]:
            husband_name = person_info["husband"]
            current_person.husband = Person.people[husband_name]

    return person_instances
    

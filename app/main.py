from typing import List, Dict, Union, Optional


class Person:
    # Class-level dictionary to store all Person instances by name
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person instance with a name and age.
        Add the instance to the class-level people dictionary.
        """
        self.name: str = name
        self.age: int = age
        # Register the Person instance in the class attribute people
        Person.people[name] = self

    def __setattr__(self, key: str, value: Optional["Person"]) -> None:
        """
        Override __setattr__ to dynamically add "wife"/"husband" attributes.
        """
        # Set the attrib. only if key isnt "wife""husband" or value is not None
        if key not in {"wife", "husband"} or value is not None:
            super().__setattr__(key, value)


def create_person_list(
    people: List[Dict[str, Union[str, int, None]]]
) -> List[Person]:
    """
    Convert a list of dictionaries into a list of Person instances.
    Link "wife" or "husband" attributes where applicable.
    """
    # Step 1: Create all Person instances first
    person_list: List[Person] = [
        Person(person["name"], person["age"]) for person in people
    ]

    # Step 2: Set relationships after all Person instances are created
    for person in people:
        current_person = Person.people[person["name"]]

        # Set the wife or husband attribute dynamically if available
        if "wife" in person and person["wife"]:
            current_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            current_person.husband = Person.people[person["husband"]]

    return person_list

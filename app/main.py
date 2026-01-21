from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    # Create initial list of Person instances
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Assign wife/husband attributes where applicable
    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            setattr(person_instance, "wife", Person.people[person["wife"]])
        elif "husband" in person and person["husband"]:
            setattr(
                person_instance,
                "husband",
                Person.people[person["husband"]]
            )

    return person_list

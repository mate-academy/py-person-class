from typing import List, Dict, Any, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[name] = self

    def __str__(self) -> str:
        return f"{self.name}, age {self.age}"


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person_instance = Person.people[name]
        if "wife" in person_data and person_data["wife"]:
            person_instance.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"]:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list

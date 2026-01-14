from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    Person.people = {}

    person_list: List[Person] = [
        Person(name=data["name"], age=data["age"]) for data in people
    ]

    for data in people:
        person = Person.people[data["name"]]

        spouse_name = data.get("wife")
        if spouse_name is not None:
            setattr(person, "wife", Person.people[spouse_name])

        spouse_name = data.get("husband")
        if spouse_name is not None:
            setattr(person, "husband", Person.people[spouse_name])

    return person_list

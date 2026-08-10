from typing import Any


class Person:

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict[str, Any]]) -> list[Person]:
    result: list[Person] = [
        Person(p_d["name"], p_d["age"]) for p_d in people
    ]
    for person, p_d in zip(result, people):
        if p_d.get("wife"):
            person.wife = p_d["wife"]  # type: ignore
        if p_d.get("husband"):
            person.husband = p_d["husband"]  # type: ignore
    for person in result:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]  # type: ignore
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]  # type: ignore

    return result

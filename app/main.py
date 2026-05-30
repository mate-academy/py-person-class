from typing import Any


class Person:
    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict[str, Any]]) -> list[Person]:
    result: list[Person] = []
    for each in people:
        result.append(Person(each["name"], each["age"]))
    for each in people:
        if each.get("wife") is not None:
            Person.people[each["wife"]].husband = Person.people[each["name"]]
        elif each.get("husband") is not None:
            Person.people[each["husband"]].wife = Person.people[each["name"]]
    return result
from typing import List


class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> List[Person]:
    result = [Person(name=data.get("name"),
                     age=data.get("age")) for data in people]

    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife \
                = Person.people[person["wife"]]

        if person.get("husband") is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return result

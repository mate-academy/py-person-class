from typing import List


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[dict]) -> List[Person]:
    Person.people = {}

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        instance = Person.people[person["name"]]
        if person.get("wife") is not None:
            instance.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())

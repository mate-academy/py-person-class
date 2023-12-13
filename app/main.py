from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(name=human["name"], age=human["age"]) for human in people
    ]

    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife = (
                Person.people.get(human["wife"]))
        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband = (
                Person.people.get(human["husband"]))

    return people_list

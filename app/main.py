from __future__ import annotations


class Person:
    people: dict
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    res_lst = [
        Person(everybody["name"], everybody["age"])
        for everybody in people
    ]
    for each in people:
        if "wife" in each.keys():
            if each["wife"] is not None:
                wife = Person.people.get(each["wife"])
                husband = Person.people.get(each["name"])
                wife.husband = husband
                husband.wife = wife
    return res_lst

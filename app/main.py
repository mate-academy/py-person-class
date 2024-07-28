from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(data["name"], data["age"]) for data in people]

    for data in people:
        name = data["name"]
        marriage_name = data.get("wife") or data.get("husband")
        person = Person.people[name]
        if marriage_name:
            marriage = Person.people.get(marriage_name)
            if "wife" in data:
                person.wife = marriage
            elif "husband" in data:
                person.husband = marriage

    return list(Person.people.values())

# I CANT SOLVE THAT ISSUE
# FAILED tests/test_main.py::
# test_person_instance_attribute_wife_and_husband_doesnt_exists
# KeyError: 'body'

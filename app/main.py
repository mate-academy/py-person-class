from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def find_partner(person: Person, spouse_name: str, is_wife: bool) -> None:
    spouse = Person.people.get(spouse_name)
    if spouse:
        if is_wife:
            person.wife = spouse
            spouse.husband = person
        else:
            person.husband = spouse
            spouse.wife = person


def create_person_list(people: list) -> list:
    created_person_list = \
        [
            Person(persona["name"], persona["age"])
            for persona in people
        ]

    for persona in people:
        person = Person.people.get(persona["name"])
        if person:
            if "wife" in persona and persona["wife"]:
                find_partner(person, persona["wife"], is_wife=True)
            if "husband" in persona and persona["husband"]:
                find_partner(person, persona["husband"], is_wife=False)

    return created_person_list

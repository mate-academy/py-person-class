from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def find_partner(self, spouse: Person, is_wife: bool) -> None:
        if is_wife:
            self.wife = spouse
            spouse.husband = self
        else:
            self.husband = spouse
            spouse.wife = self


def create_person_list(people: list) -> list:
    created_person_list = \
        [
            Person(persona["name"], persona["age"])
            for persona in people
        ]

    match_spouses(people)

    return created_person_list


def match_spouses(people_data: list) -> None:
    for persona in people_data:
        person = Person.people.get(persona["name"])
        if person:
            if wife_name := persona.get("wife"): # noqa
                spouse_name = persona["wife"]
                spouse = Person.people.get(spouse_name)
                if spouse:
                    person.find_partner(spouse, is_wife=True)
            if husband_name := persona.get("husband"): # noqa
                spouse_name = persona["husband"]
                spouse = Person.people.get(spouse_name)
                if spouse:
                    person.find_partner(spouse, is_wife=False)

from __future__ import annotations


class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []
    for person_date in people:
        person = Person(
            name=person_date["name"],
            age=person_date["age"]
        )
        Person.people[person_date["name"]] = person
        partner_status = list(person_date.keys())[2]
        if person_date[partner_status]:
            if partner_status == "wife":
                person.wife = person_date[partner_status]
            else:
                person.husband = person_date[partner_status]
        person_list.append(person)
    if len(person_list) > 1:
        for person in person_list:
            if len(list(person.__dict__.items())) > 2:
                partner_name = list(person.__dict__.items())[2][1]
                if partner_name:
                    partner_status = list(person.__dict__.items())[2][0]
                    if partner_status == "wife":
                        person.wife = Person.people[partner_name]
                    else:
                        person.husband = Person.people[partner_name]
    return person_list

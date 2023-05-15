from __future__ import annotations


class Person:
    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_new_person(self)

    @classmethod
    def add_new_person(cls, person: Person) -> None:
        cls.people.update({person.name: person})

    def add_partner(self, partner_type: str, partner_name: str) -> None:
        if partner_name not in self.people.keys():
            return
        if partner_type == "wife":
            self.wife = self.people[partner_name]
        else:
            self.husband = self.people[partner_name]


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = add_basic_info(people)
    add_partner(people)
    return person_list


def add_basic_info(people: list[dict]) -> list[Person]:
    person_list = []

    for person_dict in people:
        person_list.append(Person(person_dict["name"], person_dict["age"]))
    return person_list


def add_partner(people: list[dict]) -> None:
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict:
            person.add_partner("wife", person_dict["wife"])
        if "husband" in person_dict:
            person.add_partner("husband", person_dict["husband"])

from typing import List


class Person:
    people = {}
    people_list = []

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        Person.people[self.name] = self
        Person.people_list.append(self)


def find_partner(person_obj: Person,
                 person_to_find: str | None
                 ) -> Person | str | None:
    if person_to_find in Person.people:
        partner = person_obj.people[person_to_find]
        if hasattr(partner, "wife"):
            partner.wife = person_obj
        else:  # hasattr(partner, "husband"):
            partner.husband = person_obj
        return Person.people[person_to_find]


def create_person_list(people: List[dict]) -> List[Person]:

    for human_data in people:
        curr_person = Person(human_data["name"], human_data["age"])
        set_partner(curr_person, human_data)
    return Person.people_list


def set_partner(person: Person, person_data: dict) -> None:
    if person_data.get("wife"):
        person.wife = find_partner(person, person_data["wife"])
    elif person_data.get("husband"):
        person.husband = find_partner(person,
                                      person_data["husband"])

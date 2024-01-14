from __future__ import annotations  # for enabling user classes in annotations
from typing import Dict


class Person:
    people: Dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

        self.__class__.people[name] = self


def create_person_list(people_data: list) -> list:
    for pers in people_data:
        if "wife" in pers:
            pers["spouse_name"] = pers["wife"]
            pers["spouse_by_gender"] = "wife"
        else:
            pers["spouse_name"] = pers["husband"]
            pers["spouse_by_gender"] = "husband"

    people_list = [Person(pers["name"], pers["age"]) for pers in people_data]

    # using the fact that order is the same in `people_data` and `people_list`:
    for idx_1 in range(len(people_data) - 1):
        pers_1 = people_data[idx_1]  # a dict
        person_1 = people_list[idx_1]  # a Person
        for idx_2 in range(idx_1 + 1, len(people_data)):
            pers_2 = people_data[idx_2]
            person_2 = people_list[idx_2]

            if pers_1["spouse_name"] == pers_2["name"]:
                person_1.__dict__[pers_1["spouse_by_gender"]] = person_2
                person_2.__dict__[pers_2["spouse_by_gender"]] = person_1

    for pers in people_data:
        del pers["spouse_name"]
        del pers["spouse_by_gender"]

    return people_list

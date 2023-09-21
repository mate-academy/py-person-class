from typing import Optional


class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: Optional[int] = None
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"],
                          person_data.get("age"))
                   for person_data in people]

    relationship = [(person_data["name"],
                     person_data.get("wife"), person_data.get("husband"))
                    for person_data in people]

    for name, wife_name, husband_name in relationship:
        person = Person.people[name]

        if wife_name:
            person.wife = Person.people.get(wife_name)

        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list

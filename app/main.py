from typing import List


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: List[dict]) -> List[Person]:
    person_list: List[Person] = [Person(data["name"],
                                        data["age"]
                                        )
                                 for data in people_data]

    for data in people_data:
        current_person = Person.people.get(data["name"])
        if not current_person:
            continue

        if data.get("wife"):
            wife_person = Person.people.get(data["wife"])
            if wife_person:
                current_person.wife = wife_person
                wife_person.husband = current_person
        elif data.get("husband"):
            husband_person = Person.people.get(data["husband"])
            if husband_person:
                current_person.husband = husband_person
                husband_person.wife = current_person

    return person_list

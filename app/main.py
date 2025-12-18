from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    Person.people.clear()

    persons = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return persons

from typing import Dict, Optional, List


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def find_person(cls, name: Optional[str]) -> Optional["Person"]:
        return cls.people.get(name) if isinstance(name, str) else None


def create_person_list(people: List[dict]) -> List[Person]:
    persons = [Person(name=p.get("name"), age=p.get("age")) for p in people]

    for person in people:
        current_person = Person.find_person(person.get("name"))

        if current_person:
            wife_name = person.get("wife")
            husband_name = person.get("husband")

            if isinstance(wife_name, str):
                current_person.wife = Person.find_person(wife_name)

            if isinstance(husband_name, str):
                current_person.husband = Person.find_person(husband_name)

    return persons

from typing import List, Dict


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: List[Dict]) -> List[Person]:
    person_list = []
    for data in people_data:
        person = Person(name=data["name"], age=data["age"])
        person_list.append(person)
    for data in people_data:
        person = Person.people[data["name"]]
        if data.get("wife"):
            person.wife = Person.people[data["wife"]]
        if data.get("husband"):
            person.husband = Person.people[data["husband"]]
    return person_list

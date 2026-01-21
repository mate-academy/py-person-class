from __future__ import annotations

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def insert_person(cls, person: Person) -> None:
        cls.people[person.name] = person

    @classmethod
    def update_spouse(cls, person: Person, spouse: Person, key: str) -> None:
        if key == "husband":
            cls.people[person.name].husband = cls.people[spouse.name]
        if key == "wife":
            cls.people[person.name].wife = cls.people[spouse.name]

    @classmethod
    def is_person_in_list(cls, name: str) -> bool:
        return name in cls.people.keys()

def create_person_list(people: list[dict]) -> list[Person]:
    for p in people:
        person = Person(p["name"], p["age"])
        Person.insert_person(person)

    for p in people:
        if p.get("wife"):
            if Person.is_person_in_list(p["wife"]):
                Person.update_spouse(Person.people[p["name"]], Person.people[p["wife"]], "wife")
            elif p.get("husband"):
                if Person.is_person_in_list(p["husband"]):
                    Person.update_spouse(Person.people[p["name"]], Person.people[p["husband"]], "husband")

    return list(Person.people.values())
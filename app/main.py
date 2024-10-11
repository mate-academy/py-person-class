from typing import Optional, Dict


class Person:

    people: Dict[str, "Person"] = {}

    def __init__(self, name: str,
                 age: int,
                 spouse_name: Optional[str] = None) -> None:
        self.name: str = name
        self.age: int = age

        if spouse_name:
            self.wife: Optional[Person] = None
            self.husband: Optional[Person] = None
            self.set_spouse(spouse_name)

        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        spouse = Person.people.get(spouse_name)
        if spouse:
            if self.name in Person.people and hasattr(spouse, "husband"):
                self.wife = spouse
                spouse.husband = self
            elif self.name in Person.people and hasattr(spouse, "wife"):
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)

        person_instance = Person(name, age, spouse_name)
        person_list.append(person_instance)

    return person_list

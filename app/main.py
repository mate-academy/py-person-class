from typing import List


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[dict]) -> List[Person]:
    person_list: List[Person] = []

    # Cria as instâncias sem relacionamentos
    for person_data in people:
        person_instance = Person(person_data["name"], person_data["age"])
        person_list.append(person_instance)

    # Conecta os relacionamentos wife/husband
    for person_data in people:
        person_instance = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person_instance.wife = Person.people[person_data["wife"]]

        elif "husband" in person_data and person_data["husband"] is not None:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list

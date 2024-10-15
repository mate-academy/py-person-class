from typing import Optional


class Person:
    people: dict[str, 'Person'] = {}

    def __init__(self, name: str,  age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list[dict[str, Optional[str]]]) -> list[Person]:
    persons = []
    for person in people_list:
        new_person = Person(person["name"], person["age"])
        persons.append(new_person)
    for person in people_list:
        person.get("wife") and setattr(Person.people[person["name"]], "wife", Person.people[person["wife"]])
        person.get("husband") and setattr(Person.people[person["name"]], "husband", Person.people[person["husband"]])
    return persons

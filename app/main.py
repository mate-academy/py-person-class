from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f'Person(name="{self.name}", age={self.age})'


def create_person_list(people: List[Dict[str, object]]) -> List[Person]:
    Person.people.clear()
    name_to_person: Dict[str, Person] = {}

    for entry in people:
        person = Person(entry["name"], entry["age"])
        name_to_person[entry["name"]] = person

    for entry in people:
        person = name_to_person[entry["name"]]
        if "wife" in entry:
            wife = name_to_person.get(entry["wife"])
            if wife:
                person.wife = wife
                wife.husband = person
        if "husband" in entry:
            husband = name_to_person.get(entry["husband"])
            if husband:
                person.husband = husband
                husband.wife = person

    return list(name_to_person.values())

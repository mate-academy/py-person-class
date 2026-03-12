from typing import List, Dict, Any, Optional, Union


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: List[Dict[str, Any]]) -> List[Person]:

    Person.people = {}

    instances = [
        Person(p["name"], p["age"]) for p in people_dicts
    ]
    for person_dict in people_dicts:
        name = person_dict["name"]
        instance = Person.people[name]

        for relation in ["wife", "husband"]:
            partner_name: Optional[str] = person_dict.get(relation)
            if partner_name:
                setattr(instance, relation, Person.people[partner_name])

    return instances

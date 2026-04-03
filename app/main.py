class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


from typing import List, Dict, Optional  # noqa: E402


def create_person_list(
    people_dicts: List[Dict[str, Optional[str]]]
) -> List[Person]:
    Person.people.clear()

    person_list: List[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_dicts
    ]

    for idx, person_data in enumerate(people_dicts):
        person_instance = person_list[idx]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return person_list

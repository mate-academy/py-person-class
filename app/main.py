from typing import List, Dict, Union, Optional

class Person:
    people: Dict[str, 'Person'] = {}

    def __init__(self, name: str, age: str) -> None:
        self.name: str = name
        self.age: str = age
        self.wife: Optional['Person'] = None
        self.husband: Optional['Person'] = None

        Person.people[name] = self

def create_person_list(people: List[Dict[str, Union[str, Optional[str]]]]) -> List[Person]:
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        Person(name, age)

    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"]:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"]:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

    return list(Person.people.values())

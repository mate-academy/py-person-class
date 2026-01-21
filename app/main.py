from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self

    def set_spouse(self, spouse: Optional["Person"]) -> None:
        if spouse:
            if (self.name not in Person.people or spouse.name
                    not in Person.people):
                return

            if "wife" in self.__dict__:
                self.wife: "Person" = spouse
                spouse.husband = self
            elif "husband" in self.__dict__:
                self.husband: "Person" = spouse
                spouse.wife = self


def create_person_list(people: List[Dict[str, Optional[str]]]) -> List[Person]:
    person_list: List[Person] = []

    for person_dict in people:
        name: str = person_dict["name"]
        age: int = person_dict["age"]
        person_instance = Person(name, age)
        person_list.append(person_instance)

    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        spouse_name: Optional[str] = (person_dict.get("wife")
                                      or person_dict.get("husband"))

        if spouse_name and spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            if person_dict.get("wife"):
                person_instance.wife = spouse
                spouse.husband = person_instance
            elif person_dict.get("husband"):
                person_instance.husband = spouse
                spouse.wife = person_instance

    return person_list

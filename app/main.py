from typing import Optional, List


class Person:
    people = {}

    def __init__(self, name: str,
                 age: int,
                 spouse: Optional["Person"] = None) -> None:
        self.name = name
        self.age = age
        self.spouse = spouse
        Person.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people_data: List[dict]) -> List[Person]:
    person_list = []

    for person_data in people_data:
        name: str = person_data["name"]
        age: int = person_data["age"]
        spouse_name: Optional[str] = (person_data.get("wife")
                                      or person_data.get("husband"))

        spouse: Optional[Person] = (Person.people.get(spouse_name)
                                    if spouse_name else None)

        person = Person(name, age, spouse)
        person_list.append(person)

        if spouse:
            if "wife" in person_data:
                person.wife = spouse
            else:
                person.husband = spouse

    return person_list

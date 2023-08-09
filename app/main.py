class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_lst: list[Person] = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        person_obj: Person = Person.people[person["name"]]
        attr_name: str = "wife" if "wife" in person else "husband"
        if person.get(attr_name) is not None:
            setattr(person_obj, attr_name,
                    Person.people.get(person[attr_name]))
    return person_lst

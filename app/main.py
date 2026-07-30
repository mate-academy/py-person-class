class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [
        Person(name=p["name"], age=p["age"]) for p in people
    ]

    for p_dict in people:
        person = Person.people[p_dict["name"]]
        if p_dict.get("wife") is not None:
            person.wife = Person.people[p_dict["wife"]]
        elif p_dict.get("husband") is not None:
            person.husband = Person.people[p_dict["husband"]]

    return person_instances

class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    Person.people.clear()
    [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        if data.get("wife") is not None:
            person.wife = Person.people[data["wife"]]

        if data.get("husband") is not None:
            person.husband = Person.people[data["husband"]]

    return list(Person.people.values())

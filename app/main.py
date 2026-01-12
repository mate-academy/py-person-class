class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list: list[Person] = [
        Person(data["name"], data["age"]) for data in people
    ]

    for data in people:
        person = Person.people[data["name"]]

        if wife_name := data.get("wife"):
            person.wife = Person.people[wife_name]

        if husband_name := data.get("husband"):
            person.husband = Person.people[husband_name]

    return person_list

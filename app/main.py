class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    persons: list[Person] = [
        Person(data["name"], data["age"]) for data in people
    ]

    for data in people:
        person = Person.people[data["name"]]

        wife = data.get("wife")
        if wife is not None:
            person.wife = Person.people[wife]

        husband = data.get("husband")
        if husband is not None:
            person.husband = Person.people[husband]

    return persons

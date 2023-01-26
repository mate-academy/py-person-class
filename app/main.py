class Person:

    people: dict[str] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(
        people: list[dict[str, str | int | None]]
) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person, properties in zip(person_list, people):
        if properties.get("wife") is not None:
            person.wife = Person.people[properties["wife"]]
        elif properties.get("husband") is not None:
            person.husband = Person.people[properties["husband"]]

    return person_list

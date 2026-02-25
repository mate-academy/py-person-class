class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(
    people: list[dict[str, str | int | None]]
) -> list[Person]:
    Person.people.clear()

    person_instances: list[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        name: str = person_data["name"]
        current_person: Person = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name: str = person_data["wife"]
            current_person.wife = Person.people[wife_name]

        if (
            "husband" in person_data
            and person_data["husband"] is not None
        ):
            husband_name: str = person_data["husband"]
            current_person.husband = Person.people[husband_name]

    return person_instances

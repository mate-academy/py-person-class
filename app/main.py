class Person:
    people: dict[str, "Person"] = {}

    def __init__(self: "Person", name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    persons: list[Person] = [
        Person(person["name"], person["age"]) for person in people_data
    ]

    for person in people_data:
        instance = Person.people[person["name"]]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            attr = "wife" if "wife" in person else "husband"
            setattr(instance, attr, Person.people[spouse_name])

    return persons

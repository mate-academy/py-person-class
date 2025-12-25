class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people.clear()  # Restablecer Person.people
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in person_list:
        person_data = next(
            p for p in people if p["name"] == person.name
        )
        spouse = person_data.get("wife") or person_data.get("husband")
        if spouse:
            setattr(
                person,
                "wife" if "wife" in person_data else "husband",
                Person.people[spouse]
            )

    return person_list

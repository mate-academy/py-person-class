class Person:
    people: dict[str, "Person"] = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # Step 1: Create all Person instances (without setting spouse links)
    instances = []
    for entry in people:
        person = Person(entry["name"], entry["age"])
        instances.append(person)

    # Step 2: Set spouse relationships where applicable
    for entry in people:
        person = Person.people[entry["name"]]
        if "wife" in entry and entry["wife"] is not None:
            person.wife = Person.people[entry["wife"]]
        elif "husband" in entry and entry["husband"] is not None:
            person.husband = Person.people[entry["husband"]]

    return instances


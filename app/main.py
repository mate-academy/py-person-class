class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Person | None = None
        self.husband: Person | None = None

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result: list[Person] = []

    for entry in people:
        person = Person(entry["name"], entry["age"])
        result.append(person)

    for entry in people:
        name = entry["name"]
        current = Person.people[name]

        if "wife" in entry:
            wife_name = entry["wife"]
            if wife_name is None:
                if hasattr(current, "wife"):
                    del current.wife
            else:
                current.wife = Person.people[wife_name]

        if "husband" in entry:
            husband_name = entry["husband"]
            if husband_name is None:
                if hasattr(current, "husband"):
                    del current.husband
            else:
                current.husband = Person.people[husband_name]

    return result

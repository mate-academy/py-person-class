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
        person_name = entry["name"]
        current_person = Person.people[person_name]

        if entry.get("wife") is not None:
            wife_obj = Person.people[entry["wife"]]
            current_person.wife = wife_obj

        if entry.get("husband") is not None:
            husband_obj = Person.people[entry["husband"]]
            current_person.husband = husband_obj

    return result

class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    Person.people.clear()

    person_list = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list

class Person:

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    Person.people.clear()

    persons = [Person(entry["name"], entry["age"]) for entry in people]

    for entry in people:
        person = Person.people[entry["name"]]

        wife_name = entry.get("wife")
        husband_name = entry.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return persons

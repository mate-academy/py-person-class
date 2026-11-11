class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    persons = [Person(data["name"], data["age"]) for data in people]

    for data, person in zip(people, persons):
        wife_name = data.get("wife")
        husband_name = data.get("husband")

        if wife_name is not None:
            person.wife = Person.people[wife_name]
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return persons

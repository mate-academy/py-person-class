class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    result: list[Person] = [
        Person(item["name"], item["age"]) for item in people
    ]

    for data in people:
        current = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name is not None:
            partner = Person.people.get(wife_name)
            if partner is not None:
                current.wife = partner

        husband_name = data.get("husband")
        if husband_name is not None:
            partner = Person.people.get(husband_name)
            if partner is not None:
                current.husband = partner

    return result

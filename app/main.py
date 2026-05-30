class Person:
    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result: list[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    for person_data in people:
        if person_data.get("wife") is not None:
            Person.people[person_data["wife"]].husband = \
                Person.people[person_data["name"]]
        elif person_data.get("husband") is not None:
            Person.people[person_data["husband"]].wife = \
                Person.people[person_data["name"]]
    return result

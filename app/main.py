class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    Person.people.clear()

    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    for person_data in people_data:
        current = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            current.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            current.husband = Person.people[person_data["husband"]]

    return [Person.people[entry["name"]] for entry in people_data]

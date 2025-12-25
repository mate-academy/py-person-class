class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    persons = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_data
    ]

    for person_data in people_data:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return persons

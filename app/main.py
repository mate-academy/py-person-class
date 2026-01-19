class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:
    Person.people.clear()
    persons: list[Person] = []

    for data in people_list:
        person = Person(data["name"], data["age"])
        persons.append(person)

    for data, person in zip(people_list, persons):
        spouse_key = "wife" if "wife" in data else "husband" if "husband" in data else None
        if spouse_key and data[spouse_key] is not None:
            setattr(person, spouse_key, Person.people[data[spouse_key]])

    return persons

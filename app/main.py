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
        spouse_key = None

        if "wife" in data:
            spouse_key = "wife"
        elif "husband" in data:
            spouse_key = "husband"

        if spouse_key and data[spouse_key] is not None:
            spouse_name = data[spouse_key]
            setattr(person, spouse_key, Person.people[spouse_name])

    return persons

class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    person_list: list[Person] = []

    for person_data in people:
        name: str = person_data["name"]
        age: int = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        person: Person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return person_list

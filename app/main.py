class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person in people:
        person_instance = Person.people[person.get("name")]

        if person.get("wife"):
            person_instance.wife = Person.people[person.get("wife")]

        if person.get("husband"):
            person_instance.husband = Person.people[person.get("husband")]

    return person_list

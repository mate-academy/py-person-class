class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def add_husband_wife_if_merried(self, person: dict) -> None:
        if person.get("wife") is not None:
            self.wife = Person.people.get(person.get("wife"))

        if person.get("husband") is not None:
            self.husband = Person.people.get(person.get("husband"))


def create_person_list(people: list) -> list:
    for person in people:
        Person(
            name=person.get("name"),
            age=person.get("age"),
        )
    for person in people:
        Person.people[person.get("name")].add_husband_wife_if_merried(person)

    return [person for person in Person.people.values()]

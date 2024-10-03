class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list[dict[str | int | None]]) -> list[Person]:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]

    return person_list

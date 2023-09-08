class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person.get("name"), person.get("age")) for person in people
    ]
    for persons in people:
        if persons.get("wife"):
            Person.people[persons.get("name")].wife = (
                Person.people[persons.get("wife")]
            )
        elif persons.get("husband"):
            Person.people[persons.get("name")].husband = (
                Person.people[persons.get("husband")]
            )
    return person_list

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person.get("name"), person.get("age")) for person in people
    ]

    for person in people:
        if wife := person.get("wife"):
            Person.people[person.get("name")].wife \
                = Person.people[wife]

        if husband := person.get("husband"):
            Person.people[person.get("name")].husband \
                = Person.people[husband]

    return person_list

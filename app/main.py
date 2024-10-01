class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def weddings(self, other: "Person") -> None:
        self.wife = other
        other.husband = self


def create_person_list(people: list) -> list:
    [Person(person.get("name"), person.get("age")) for person in people]
    for person in people:
        if wife := person.get("wife"):
            (Person.people.get(person.get("name"))
             .weddings(Person.people.get(wife)))
    return list(Person.people.values())

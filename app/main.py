class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        Person.people[name] = self
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    persons: list[Person] = []

    for person in people:
        persons.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband \
                = Person.people[person["name"]]
    return persons

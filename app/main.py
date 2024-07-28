class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(name=person["name"], age=person["age"])

    for person in people:
        name = person["name"]

        if pair := person.get("husband"):
            Person.people[name].husband = Person.people[pair]
            Person.people[pair].wife = Person.people[name]

    return list(Person.people.values())

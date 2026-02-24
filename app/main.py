class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    [Person(human.get("name"), human.get("age")) for human in people]

    for person in people:
        human = Person.people.get(person.get("name"))
        if person.get("wife", None):
            human.wife = Person.people.get(person.get("wife"))

        if person.get("husband", None):
            human.husband = Person.people.get(person.get("husband"))

    return list(Person.people.values())

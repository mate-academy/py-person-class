class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(human.get("name"), human.get("age")) for human in people
    ]

    for human in people:
        person = Person.people.get(human.get("name"))
        if human.get("wife") is not None:
            person.wife = Person.people.get(human.get("wife"))
        elif human.get("husband") is not None:
            person.husband = Person.people.get(human.get("husband"))
    return person_instances

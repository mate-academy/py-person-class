class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        _ = Person(name=person.get("name"), age=person.get("age"))

    for person in people:
        person_name = person.get("name")

        if (wife := person.get("wife")) is not None:
            Person.people[person_name].wife = Person.people[wife]
            continue

        if (husband := person.get("husband")) is not None:
            Person.people[person_name].husband = Person.people[husband]

    return [person for person in Person.people.values()]

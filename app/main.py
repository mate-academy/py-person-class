class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    instances = [
        Person
        (
            single_person["name"],
            single_person["age"]
        )
        for single_person in people
    ]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[
                person["name"]
            ].husband = Person.people[person["husband"]]
    return instances
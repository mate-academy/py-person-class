class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    person_list = [Person(dc["name"], dc["age"]) for dc in people]

    for dc in people:

        if dc.get("wife"):
            Person.people[dc["name"]].wife = Person.people[dc["wife"]]

        if dc.get("husband"):
            Person.people[dc["name"]].husband = (
                Person.people)[dc["husband"]]

    return person_list

class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for dc in people:
        _ = Person(dc["name"], dc["age"])

    for dc in people:

        if "wife" in dc:
            if dc["wife"] is not None:
                Person.people[dc["name"]].wife = Person.people[dc["wife"]]

        if "husband" in dc:
            if dc["husband"] is not None:
                Person.people[dc["name"]].husband = (
                    Person.people)[dc["husband"]]

        person_list.append(Person.people[dc["name"]])

    return person_list

class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    out = [Person(person["name"], person["age"]) for person in people]

    for i, data in enumerate(people):
        if data.get("wife"):
            out[i].wife = Person.people[data["wife"]]

        if data.get("husband"):
            out[i].husband = Person.people[data["husband"]]

    return out

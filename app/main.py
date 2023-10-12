class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    pep = [Person(p["name"], p["age"]) for p in people]
    for i, p in enumerate(people):
        try:
            if p["wife"] is not None:
                pep[i].wife = Person.people[p["wife"]]
        except KeyError:
            if p["husband"] is not None:
                pep[i].husband = Person.people[p["husband"]]

    return pep

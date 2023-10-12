class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    pep = [Person(p["name"], p["age"]) for p in people]
    for i, pop in enumerate(people):
        try:
            if pop["wife"] is not None:
                pep[i].wife = Person.people[pop["wife"]]
        except KeyError:
            if pop["husband"] is not None:
                pep[i].husband = Person.people[pop["husband"]]

    return pep

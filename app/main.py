class Person:
    people = {}
    pass

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for p in people:
        Person(p["name"], p["age"])

    for p in people:
        if "wife" in p and p["wife"] is not None:
            Person.people[p["name"]].wife = Person.people[p["wife"]]
        if "husband" in p and p["husband"] is not None:
            Person.people[p["name"]].husband = Person.people[p["husband"]]
    return list(Person.people.values())

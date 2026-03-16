class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person = Person.people[p["name"]]

        if p.get("wife"):
            person.wife = Person.people[p["wife"]]

        if p.get("husband"):
            person.husband = Person.people[p["husband"]]

    return person_list
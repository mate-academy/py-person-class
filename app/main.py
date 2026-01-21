class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]
    person_list = [Person.people[person["name"]] for person in people]
    for person in people:
        individual = Person.people[person["name"]]
        if person.get("wife"):
            individual.__dict__["wife"] = Person.people[person["wife"]]
        if person.get("husband"):
            individual.__dict__["husband"] = Person.people[person["husband"]]
    return person_list

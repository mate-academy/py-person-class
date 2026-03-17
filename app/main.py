class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        current = Person.people[person["name"]]

        if person.get("wife"):
            current.wife = Person.people[person["wife"]]

        if person.get("husband"):
            current.husband = Person.people[person["husband"]]
    return result

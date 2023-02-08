class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for man in people:
        if man.get("wife"):
            Person.people[man["name"]].wife = Person.people[man["wife"]]
            Person.people[man["wife"]].husband = Person.people[man["name"]]
    return person_list

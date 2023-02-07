class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for prsn in people:
        if prsn.get("wife"):
            Person.people[prsn["name"]].wife = Person.people[prsn["wife"]]
            Person.people[prsn["wife"]].husband = Person.people[prsn["name"]]
    return person_list

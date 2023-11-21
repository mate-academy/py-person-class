class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]])
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
    return [Person.people[key] for key in Person.people]
